#include <Arduino_OV767X.h>

unsigned short pixels[320 * 240];

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!Camera.begin(QVGA, RGB565, 1)) {
    Serial.print("err");
    while (1);
  }
}

void loop() {
  if (Serial.read() == 'c') {
    Camera.readFrame(pixels);

    int numPixels = Camera.width() * Camera.height();

    for (int i = 0; i < numPixels; i++) {
      unsigned short p = pixels[i];

      if (p < 0x1000) {
        Serial.print('0');
      }

      if (p < 0x0100) {
        Serial.print('0');
      }

      if (p < 0x0010) {
        Serial.print('0');
      }

      Serial.print(p, HEX);
    }
  }
}
