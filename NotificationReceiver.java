package org.test.asy;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;

public class NotificationReceiver extends BroadcastReceiver {

  @Override
  public void onReceive(Context context, Intent intent) {
    context.startService(new Intent(context, ServiceNotify.class));
  }
}