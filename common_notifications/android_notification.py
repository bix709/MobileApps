import plyer
from jnius import autoclass
from plyer.facades import Notification
from plyer.platforms.android import activity, SDK_INT

AndroidString = autoclass('java.lang.String')
Context = autoclass('android.content.Context')
NotificationBuilder = autoclass('android.app.Notification$Builder')
Drawable = autoclass("{}.R$drawable".format(activity.getPackageName()))
Intent = autoclass('android.content.Intent')
NotificationClass = autoclass('android.app.Notification')
PendingIntent = autoclass('android.app.PendingIntent')

notificationIntent = activity.getPackageManager().getLaunchIntentForPackage(activity.getPackageName())
notificationIntent.setFlags(
    Intent.FLAG_ACTIVITY_CLEAR_TOP |
    Intent.FLAG_ACTIVITY_SINGLE_TOP)
intent = PendingIntent.getActivity(activity, 0, notificationIntent, 0)


class AndroidNotification(Notification):
    def _get_notification_service(self):
        if not hasattr(self, '_ns'):
            self._ns = activity.getSystemService(Context.NOTIFICATION_SERVICE)
        return self._ns

    def _notify(self, **kwargs):
        icon = getattr(Drawable, kwargs.get('icon_android', 'icon'))
        noti = NotificationBuilder(activity)
        noti.setContentTitle(AndroidString(
            kwargs.get('title').encode('utf-8')))
        noti.setContentText(AndroidString(
            kwargs.get('message').encode('utf-8')))
        noti.setTicker(AndroidString(
            kwargs.get('ticker').encode('utf-8')))
        noti.setSmallIcon(icon)
        noti.defaults |= NotificationClass.DEFAULT_LIGHTS
        noti.setPriority(NotificationClass.PRIORITY_HIGH)
        noti.setAutoCancel(True)
        noti.setContentIntent(intent)

        if SDK_INT >= 16:
            noti = noti.build()
        else:
            noti = noti.getNotification()
        plyer.vibrator.vibrate(1)
        self._get_notification_service().notify(0, noti)


def instance():
    return AndroidNotification()
