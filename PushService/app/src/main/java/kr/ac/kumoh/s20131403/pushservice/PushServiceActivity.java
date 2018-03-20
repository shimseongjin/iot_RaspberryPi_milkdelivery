package kr.ac.kumoh.s20131403.pushservice;

import android.app.Activity;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

public  class  PushServiceActivity extends AppCompatActivity {
    public static String alarm="dd 21.0 dd 17.0";
    public static TextView text1;
    public static TextView text2;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_push_service);
    }
    public void onclick(View v){
        String[] a=alarm.split(" ");

        text1=(TextView)findViewById(R.id.temp);
        text1.setText(a[1]+'℃');
        text2=(TextView)findViewById(R.id.hum);
        text2.setText(a[3]+'%');
    }
}