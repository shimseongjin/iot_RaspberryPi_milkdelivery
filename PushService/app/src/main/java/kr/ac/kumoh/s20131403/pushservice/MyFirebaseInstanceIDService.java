package kr.ac.kumoh.s20131403.pushservice;
/**
 * Created by 혜민 on 2017-11-24.
 */

import android.util.Log;

import com.google.firebase.iid.FirebaseInstanceId;
import com.google.firebase.iid.FirebaseInstanceIdService;

public class MyFirebaseInstanceIDService extends FirebaseInstanceIdService {
    private static final String TAG = "MyFirebaseIIDService";
    // [START refresh_token]
       @Override
        public void onTokenRefresh() {
           // Get updated InstanceID token.
                   String refreshedToken = FirebaseInstanceId.getInstance().getToken();
                   Log.d(TAG, "Refreshed token: " + refreshedToken);
                   sendRegistrationToServer(refreshedToken);
       }
                   // [END refresh_token]
        private void sendRegistrationToServer(String token) {
           // TODO: Implement this method to send token to your app server.
        }
}

