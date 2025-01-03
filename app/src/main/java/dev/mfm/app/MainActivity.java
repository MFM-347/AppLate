package dev.mfm.app;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;
import com.google.android.material.color.DynamicColors;
import dev.mfm.app.databinding.ActivityMainBinding;

public class MainActivity extends AppCompatActivity {

  private ActivityMainBinding binding;

  @Override
  protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    DynamicColors.applyToActivityIfAvailable(this);
    binding = ActivityMainBinding.inflate(getLayoutInflater());
    setContentView(binding.getRoot());
    Switch darkModeSwitch = findViewById(R.id.darkModeSwitch);
    darkModeSwitch.setOnCheckedChangeListener((buttonView, isChecked) -> {
      AppCompatDelegate.setDefaultNightMode(
        isChecked
          ? AppCompatDelegate.MODE_NIGHT_YES
          : AppCompatDelegate.MODE_NIGHT_NO
      );
    });
  }

  @Override
  protected void onDestroy() {
    super.onDestroy();
    this.binding = null;
  }
}
