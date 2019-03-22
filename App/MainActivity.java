package com.example.shakedemo;

import android.Manifest;
import android.content.pm.PackageManager;
import android.os.Bundle;

import android.app.Activity;
import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Environment;
import android.support.v4.content.ContextCompat;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.content.Context;
import android.widget.Toast;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

import static java.lang.String.*;


public class MainActivity extends Activity implements SensorEventListener {
    private float mLastX, mLastY, mLastZ;
    private boolean mInitialized;
    private SensorManager mSensorManager;
    private Sensor mAccelerometer;
    private final float NOISE = (float) 0.1;
    public SampleRate sampleRate;
    private FileWriter writer;
    File root, dir, sensorFile;
    private String PATH;
    ArrayList<String> list;
    private FileOutputStream f;
    private File file;



    /** Called when the activity is first created. */

    @Override
//    @TargetApi(19)
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
//        try {
//            if(checkPermssion(Manifest.permission.WRITE_EXTERNAL_STORAGE)) {

//                file = new File(Environment.getExternalStorageDirectory().getAbsolutePath(), "output.txt");
//                file = new File(getApplicationContext().getFilesDir().getPath(), "output.txt");
//                f = new FileOutputStream(file);
//            }
//            else {
//                Toast.makeText(this, "Cannot Write to Externel Storage.", Toast.LENGTH_SHORT).show();
//            }
//        }catch (FileNotFoundException e){
//            e.printStackTrace();
//        }
        try {
            root = android.os.Environment.getExternalStorageDirectory();
            dir = new File(root.getAbsolutePath() + "/myapp");
            dir.mkdirs();
        //        sensorFile = new File(dir, "data.txt");
            file = new File(dir, "output.txt");
            f = new FileOutputStream(file);
        }catch (FileNotFoundException e){
            e.printStackTrace();
        }

        mInitialized = false;
        mSensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        mAccelerometer = mSensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
//        mSensorManager.registerListener(this, mAccelerometer, SensorManager.SENSOR_DELAY_NORMAL);
//        mSensorManager.registerListener(this, mAccelerometer,sampleRate.get_SENSOR_RATE_FAST());
//        sampleRate = new SampleRate();

    }

//    @TargetApi(19)

    public void onStartClick(View view) {
        mSensorManager.registerListener(this, mAccelerometer, SensorManager.SENSOR_DELAY_NORMAL);

}

    public void onStopClick(View view) {
        mSensorManager.unregisterListener(this);
        try {
            f.close();
        }catch (IOException e){
            e.printStackTrace();
        }
    }

    protected void onResume() {
        super.onResume();

//        mSensorManager.registerListener(this, mAccelerometer, SensorManager.SENSOR_DELAY_NORMAL);
//        try{
//            writer = new FileWriter("data.txt", true);
//        }catch (IOException e){
//            e.printStackTrace();
//        }
//        mSensorManager.registerListener(this, mAccelerometer, sampleRate.get_SENSOR_RATE_FAST())



    }
    protected void onPause() {
        super.onPause();

//        mSensorManager.unregisterListener(this);
//        if (writer != null ){
//            try{
//                writer.close();
//            }catch (IOException e){
//                e.printStackTrace();
//            }
//        }
    }
//    protected void onStop() {
//        // unregister listener
//        mSensorManager.unregisterListener(this);
//        super.onStop();
//    }
//    protected void onStop(){
//        mSensorManager.unregisterListener(this);
//        super.onStop();
//    }
    public boolean checkPermssion(String permission){
        int check = ContextCompat.checkSelfPermission(this,permission);
        return (check == PackageManager.PERMISSION_GRANTED);
    }
    private boolean isExternalStorageWritable(){
        if(Environment.MEDIA_MOUNTED.equals(Environment.getExternalStorageState())){
            Log.i("State", "Yes, it is writable!");
            return true;
        }else{
            return false;
        }
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {
// can be safely ignored for this demo
    }
    @Override
    public void onSensorChanged(SensorEvent event) {

        TextView tvX = (TextView) findViewById(R.id.x_axis);
        TextView tvY = (TextView) findViewById(R.id.y_axis);
        TextView tvZ = (TextView) findViewById(R.id.z_axis);
        ImageView iv = (ImageView) findViewById(R.id.image);
        float x = event.values[0];
        float y = event.values[1];
        float z = event.values[2];

        if (!mInitialized) {
//            mLastX = x;
//            mLastY = y;
//            mLastZ = z;
            tvX.setText("0.0");
            tvY.setText("0.0");
            tvZ.setText("0.0");
            mInitialized = true;
        } else {
//            float deltaX = Math.abs(mLastX - x);
//            float deltaY = Math.abs(mLastY - y);
//            float deltaZ = Math.abs(mLastZ - z);
//            if (deltaX < NOISE) deltaX = (float) 0.0;
//            if (deltaY < NOISE) deltaY = (float) 0.0;
//            if (deltaZ < NOISE) deltaZ = (float) 0.0;
//            if (x < NOISE) x = (float) 0.0;
//            if (y < NOISE) y = (float) 0.0;
//            if (z < NOISE) z = (float) 0.0;
//            mLastX = x;
//            mLastY = y;
//            mLastZ = z;
//            tvX.setText(Float.toString(deltaX));
//            tvY.setText(Float.toString(deltaY));
//            tvZ.setText(Float.toString(deltaZ));
            tvX.setText(Float.toString(x));
            tvY.setText(Float.toString(y));
            tvZ.setText(Float.toString(z));
            iv.setVisibility(View.VISIBLE);


//            list.add(Float.toString(deltaX) + "," + Float.toString(deltaY) + "," + Float.toString(deltaY) + "\n");

//            try{
//                if(checkPermssion(Manifest.permission.WRITE_EXTERNAL_STORAGE)) {

//                File sdCard = Environment.getExternalStorageDirectory();
//                File dir = new File(sdCard.getAbsolutePath() + "/nick");
//                Boolean dirsMade = dir.mkdir();
//                dir.mkdirs();
//                Log.v("Accel", dirsMade.toString());

//                    File file = new File(Environment.getExternalStorageDirectory().getAbsolutePath(), "output.txt");
//                    FileOutputStream f = new FileOutputStream(file, true);

                    try {
//                        f.write(format("%s,%s,%s\n", Float.toString(deltaX), Float.toString(deltaY), Float.toString(deltaZ)).getBytes());
                        f.write(format("%s,%s,%s\n", Float.toString(x), Float.toString(y), Float.toString(z)).getBytes());

//                        f.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
//                }
//            }catch (FileNotFoundException e){
//                e.printStackTrace();
//            }

//            try{
//                writer.write(deltaX+","+deltaY+","+deltaY+"\n");
//            }catch (IOException e){
//                e.printStackTrace();
//            }
//            if (count % 1000 == 0) {
//                tvX.setText(Float.toString(deltaX));
//                tvY.setText(Float.toString(deltaY));
//                tvZ.setText(Float.toString(deltaZ));
//                iv.setVisibility(View.VISIBLE);
//                {
//            if (deltaX > deltaY) {
//                iv.setImageResource(R.drawable.horizontal);
//            } else if (deltaY > deltaX) {
//                iv.setImageResource(R.drawable.vertical);
//            } else {
//                iv.setVisibility(View.INVISIBLE);
//                    }

        }
    }
}
