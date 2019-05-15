// This file is generated by Simplicity Studio.  Please do not edit manually.
//
//

#include PLATFORM_HEADER
#include CONFIGURATION_HEADER
#include "af.h"

// Init function declarations.
void emberAfInit(void);
void emberAfMainInitCallback(void);

void emAfInit(void)
{
  emberAfInit();
  emberAfMainInitCallback();
}

// Tick function declarations.
void emberAfMainTickCallback(void);
void emberAfTick(void);

void emAfTick(void)
{
  emberAfMainTickCallback();
  emberAfTick();
}

void emAfResetAttributes(uint8_t endpointId)
{
}

// PreCommandReceived function declarations.
bool emberAfPreCommandReceivedCallback(EmberAfClusterCommand* cmd);

bool emAfPreCommandReceived(EmberAfClusterCommand* cmd)
{
  return emberAfPreCommandReceivedCallback(cmd);
}

// PreZDOMessageReceived function declarations.
bool emberAfPreZDOMessageReceivedCallback(EmberNodeId emberNodeId,EmberApsFrame* apsFrame,uint8_t* message,uint16_t length);

bool emAfPreZDOMessageReceived(EmberNodeId emberNodeId,EmberApsFrame* apsFrame,uint8_t* message,uint16_t length)
{
  return emberAfPreZDOMessageReceivedCallback(emberNodeId, apsFrame, message, length);
}

// RetrieveAttributeAndCraftResponse function declarations.
bool emAfPluginGreenPowerClientRetrieveAttributeAndCraftResponse(uint8_t endpoint, EmberAfClusterId clusterId, EmberAfAttributeId attrId, uint8_t mask, uint16_t maunfacturerCode, uint16_t readLength);

bool emAfRetrieveAttributeAndCraftResponse(uint8_t endpoint, EmberAfClusterId clusterId, EmberAfAttributeId attrId, uint8_t mask, uint16_t maunfacturerCode, uint16_t readLength)
{
  return emAfPluginGreenPowerClientRetrieveAttributeAndCraftResponse(endpoint, clusterId, attrId, mask, maunfacturerCode, readLength);
}

// ZigbeeKeyEstablishment function declarations.
void emberAfPluginUpdateTcLinkKeyZigbeeKeyEstablishmentCallback(EmberEUI64 partner, EmberKeyStatus status);
void emberAfZigbeeKeyEstablishmentCallback(EmberEUI64 partner, EmberKeyStatus status);

void emAfZigbeeKeyEstablishment(EmberEUI64 partner, EmberKeyStatus status)
{
  emberAfPluginUpdateTcLinkKeyZigbeeKeyEstablishmentCallback(partner, status);
  emberAfZigbeeKeyEstablishmentCallback(partner, status);
}

// ReadAttributesResponse function declarations.
bool emberAfReadAttributesResponseCallback(EmberAfClusterId clusterId,uint8_t* buffer,uint16_t bufLen);

bool emAfReadAttributesResponse(EmberAfClusterId clusterId,uint8_t* buffer,uint16_t bufLen)
{
  return emberAfReadAttributesResponseCallback(clusterId, buffer, bufLen);
}

// ReportAttributes function declarations.
bool emberAfReportAttributesCallback(EmberAfClusterId clusterId,uint8_t * buffer,uint16_t bufLen);

bool emAfReportAttributes(EmberAfClusterId clusterId,uint8_t * buffer,uint16_t bufLen)
{
  return emberAfReportAttributesCallback(clusterId, buffer, bufLen);
}
