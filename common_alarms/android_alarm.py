from jnius import autoclass
from plyer.platforms.android import activity
from android.broadcast import BroadcastReceiver


AndroidString = autoclass('java.lang.String')
Context = autoclass('android.content.Context')
NotificationBuilder = autoclass('android.app.Notification$Builder')
Drawable = autoclass("{}.R$drawable".format(activity.getPackageName()))
Intent = autoclass('android.content.Intent')
NotificationClass = autoclass('android.app.Notification')
PendingIntent = autoclass('android.app.PendingIntent')

SystemClock = autoclass('android.os.SystemClock')
AlarmManager = autoclass('android.app.AlarmManager')
PENDING_INTENT_REQUEST_CODE = 889754

# service = autoclass('org.test.android.PythonService').mService


def schedule_alarm_manager(interval, callback):
    intent = Intent(Intent.ACTION_PROVIDER_CHANGED)
    pi = PendingIntent.getBroadcast(activity, PENDING_INTENT_REQUEST_CODE, intent, 0)
    am = activity.getSystemService(Context.ALARM_SERVICE)
    am.setRepeating(AlarmManager.RTC_WAKEUP, SystemClock.currentTimeMillis(), interval * 1000, pi)
    br = BroadcastReceiver(callback, ['provider_changed'])
    br.context = activity
    br.start()
