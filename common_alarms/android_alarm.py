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
AndroidAlarmManager = autoclass('android.app.AlarmManager')
PENDING_INTENT_REQUEST_CODE = 889754


class AlarmManager(object):
    def __init__(self, event):
        super(AlarmManager, self).__init__()
        self.event = event
        self.alarm_manager = None
        self.broadcast_receiver = None
        self.pending_intent = PendingIntent.getBroadcast(activity, PENDING_INTENT_REQUEST_CODE,
                                                         Intent(AndroidString(self.event)), 0)

    def schedule_interval(self, interval, callback):
        self.alarm_manager = activity.getSystemService(Context.ALARM_SERVICE)
        self.alarm_manager.setRepeating(AndroidAlarmManager.RTC_WAKEUP,
                                        SystemClock.elapsedRealtime(),
                                        interval * 1000, self.pending_intent)
        self.broadcast_receiver = BroadcastReceiver(callback, [self.event])
        self.broadcast_receiver.start()

    def stop_alarm(self):
        self.alarm_manager.cancel(self.pending_intent)
        self.pending_intent.cancel()
