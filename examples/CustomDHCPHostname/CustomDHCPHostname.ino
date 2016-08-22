/*
 * UIPEthernet CustomDHCPHostname example.
 * Author: Brian Atwell
 *
 * UIPEthernet is a TCP/IP stack that can be used with a enc28j60 based
 * Ethernet-shield.
 *
 * UIPEthernet uses the fine uIP stack by Adam Dunkels <adam@sics.se>
 *
 *      -----------------
 *
 * This Hello World example sets up a custom hostname on DHCP server
 *
 */

#include <UIPEthernet.h>

EthernetServer server = EthernetServer(80);

void setup()
{
  int etherResults = 0;
  Serial.begin(9600);

  uint8_t mac[6] = {0x6A, 0x70, 0xF7, 0xEB, 0x80, 0x8D};

  Ethernet.begin(mac, "HelloWorldArduino");

  Serial.print("Ethernet.begin: ");

  server.begin();

  Serial.print("IP Address: ");
  Serial.println(UIPEthernet.localIP());
  Serial.print("Default Gateway: ");
  Serial.println(UIPEthernet.gatewayIP());
  Serial.print("DNS Server: ");
  Serial.println(UIPEthernet.dnsServerIP());
}

void loop()
{
  size_t size;
  boolean isAlive = true;
  // give the web browser time to receive the data
  delay(1);
}
