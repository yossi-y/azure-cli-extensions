# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['peering '] = """
    type: group
    short-summary: peering 
"""

helps['peering  check-service-provider-availability'] = """
    type: command
    short-summary: Checks if the peering service provider is present within 1000 miles of customer's location
    examples:
      - name: Check if peering service provider is available in customer location
        text: |-
               az peering  check-service-provider-availability --peering-service-location "peeringServiceLocation1" --p\
eering-service-provider "peeringServiceProvider1"
"""

helps['peering legacy-peering'] = """
    type: group
    short-summary: peering legacy-peering
"""

helps['peering legacy-peering list'] = """
    type: command
    short-summary: Lists all of the legacy peerings under the given subscription matching the specified kind and locati\
on.
    examples:
      - name: List legacy peerings
        text: |-
               az peering legacy-peering list --kind "Exchange" --peering-location "peeringLocation0"
"""

helps['peering asn'] = """
    type: group
    short-summary: peering asn
"""

helps['peering asn list'] = """
    type: command
    short-summary: Lists all of the peer ASNs under the given subscription.
    examples:
      - name: List peer ASNs in a subscription
        text: |-
               az peering asn list
"""

helps['peering asn show'] = """
    type: command
    short-summary: Gets the peer ASN with the specified name under the given subscription.
    examples:
      - name: Get a peer ASN
        text: |-
               az peering asn show --name "peerAsnName"
"""

helps['peering asn create'] = """
    type: command
    short-summary: Creates a new peer ASN or updates an existing peer ASN with the specified name under the given subsc\
ription.
    examples:
      - name: Create a peer ASN
        text: |-
               az peering asn create --peer-asn 65000 --peer-contact-detail email="noc@contoso.com" phone="+1 (234) 567\
-8999" role="Noc" --peer-contact-detail email="abc@contoso.com" phone="+1 (234) 567-8900" role="Policy" --peer-contact-\
detail email="xyz@contoso.com" phone="+1 (234) 567-8900" role="Technical" --peer-name "Contoso" --name "peerAsnName"
"""

helps['peering asn update'] = """
    type: command
    short-summary: Creates a new peer ASN or updates an existing peer ASN with the specified name under the given subsc\
ription.
    examples:
      - name: Create a peer ASN
        text: |-
               az peering asn update --peer-asn 65000 --peer-contact-detail email="noc@contoso.com" phone="+1 (234) 567\
-8999" role="Noc" --peer-contact-detail email="abc@contoso.com" phone="+1 (234) 567-8900" role="Policy" --peer-contact-\
detail email="xyz@contoso.com" phone="+1 (234) 567-8900" role="Technical" --peer-name "Contoso" --name "peerAsnName"
"""

helps['peering asn delete'] = """
    type: command
    short-summary: Deletes an existing peer ASN with the specified name under the given subscription.
    examples:
      - name: Delete a peer ASN
        text: |-
               az peering asn delete --name "peerAsnName"
"""

helps['peering peering-location'] = """
    type: group
    short-summary: peering peering-location
"""

helps['peering peering-location list'] = """
    type: command
    short-summary: Lists all of the available peering locations for the specified kind of peering.
    examples:
      - name: List direct peering locations
        text: |-
               az peering peering-location list --kind "Direct"
      - name: List exchange peering locations
        text: |-
               az peering peering-location list --kind "Exchange"
"""

helps['peering registered-asn'] = """
    type: group
    short-summary: peering registered-asn
"""

helps['peering registered-asn list'] = """
    type: command
    short-summary: Lists all registered ASNs under the given subscription, resource group and peering.
    examples:
      - name: List all the registered ASNs associated with the peering
        text: |-
               az peering registered-asn list --peering-name "peeringName" --resource-group "rgName"
"""

helps['peering registered-asn show'] = """
    type: command
    short-summary: Gets an existing registered ASN with the specified name under the given subscription, resource group\
 and peering.
    examples:
      - name: Get a registered ASN associated with the peering
        text: |-
               az peering registered-asn show --peering-name "peeringName" --name "registeredAsnName0" --resource-group\
 "rgName"
"""

helps['peering registered-asn create'] = """
    type: command
    short-summary: Creates a new registered ASN with the specified name under the given subscription, resource group an\
d peering.
    examples:
      - name: Create or update a registered ASN for the peering
        text: |-
               az peering registered-asn create --peering-name "peeringName" --asn 65000 --name "registeredAsnName" --r\
esource-group "rgName"
"""

helps['peering registered-asn update'] = """
    type: command
    short-summary: Creates a new registered ASN with the specified name under the given subscription, resource group an\
d peering.
    examples:
      - name: Create or update a registered ASN for the peering
        text: |-
               az peering registered-asn update --peering-name "peeringName" --asn 65000 --name "registeredAsnName" --r\
esource-group "rgName"
"""

helps['peering registered-asn delete'] = """
    type: command
    short-summary: Deletes an existing registered ASN with the specified name under the given subscription, resource gr\
oup and peering.
    examples:
      - name: Deletes a registered ASN associated with the peering
        text: |-
               az peering registered-asn delete --peering-name "peeringName" --name "registeredAsnName" --resource-grou\
p "rgName"
"""

helps['peering registered-prefix'] = """
    type: group
    short-summary: peering registered-prefix
"""

helps['peering registered-prefix list'] = """
    type: command
    short-summary: Lists all registered prefixes under the given subscription, resource group and peering.
    examples:
      - name: List all the registered prefixes associated with the peering
        text: |-
               az peering registered-prefix list --peering-name "peeringName" --resource-group "rgName"
"""

helps['peering registered-prefix show'] = """
    type: command
    short-summary: Gets an existing registered prefix with the specified name under the given subscription, resource gr\
oup and peering.
    examples:
      - name: Get a registered prefix associated with the peering
        text: |-
               az peering registered-prefix show --peering-name "peeringName" --name "registeredPrefixName" --resource-\
group "rgName"
"""

helps['peering registered-prefix create'] = """
    type: command
    short-summary: Creates a new registered prefix with the specified name under the given subscription, resource group\
 and peering.
    examples:
      - name: Create or update a registered prefix for the peering
        text: |-
               az peering registered-prefix create --peering-name "peeringName" --prefix "10.22.20.0/24" --name "regist\
eredPrefixName" --resource-group "rgName"
"""

helps['peering registered-prefix update'] = """
    type: command
    short-summary: Creates a new registered prefix with the specified name under the given subscription, resource group\
 and peering.
    examples:
      - name: Create or update a registered prefix for the peering
        text: |-
               az peering registered-prefix update --peering-name "peeringName" --prefix "10.22.20.0/24" --name "regist\
eredPrefixName" --resource-group "rgName"
"""

helps['peering registered-prefix delete'] = """
    type: command
    short-summary: Deletes an existing registered prefix with the specified name under the given subscription, resource\
 group and peering.
    examples:
      - name: Deletes a registered prefix associated with the peering
        text: |-
               az peering registered-prefix delete --peering-name "peeringName" --name "registeredPrefixName" --resourc\
e-group "rgName"
"""

helps['peering peering'] = """
    type: group
    short-summary: peering peering
"""

helps['peering peering list'] = """
    type: command
    short-summary: Lists all of the peerings under the given subscription.
    examples:
      - name: List peerings in a resource group
        text: |-
               az peering peering list --resource-group "rgName"
"""

helps['peering peering show'] = """
    type: command
    short-summary: Gets an existing peering with the specified name under the given subscription and resource group.
    examples:
      - name: Get a peering
        text: |-
               az peering peering show --name "peeringName" --resource-group "rgName"
"""

helps['peering peering create'] = """
    type: command
    short-summary: Creates a new peering or updates an existing peering with the specified name under the given subscri\
ption and resource group.
    examples:
      - name: Create a direct peering
        text: |-
               az peering peering create --kind "Direct" --location "eastus" --direct "{\\"connections\\":[{\\"bandwidt\
hInMbps\\":10000,\\"bgpSession\\":{\\"maxPrefixesAdvertisedV4\\":1000,\\"maxPrefixesAdvertisedV6\\":100,\\"md5Authentic\
ationKey\\":\\"test-md5-auth-key\\",\\"sessionPrefixV4\\":\\"192.168.0.0/31\\",\\"sessionPrefixV6\\":\\"fd00::0/127\\"}\
,\\"connectionIdentifier\\":\\"5F4CB5C7-6B43-4444-9338-9ABC72606C16\\",\\"peeringDBFacilityId\\":99999,\\"sessionAddres\
sProvider\\":\\"Peer\\",\\"useForPeeringService\\":false},{\\"bandwidthInMbps\\":10000,\\"connectionIdentifier\\":\\"8A\
B00818-D533-4504-A25A-03A17F61201C\\",\\"peeringDBFacilityId\\":99999,\\"sessionAddressProvider\\":\\"Microsoft\\",\\"u\
seForPeeringService\\":true}],\\"directPeeringType\\":\\"Edge\\",\\"peerAsn\\":{\\"id\\":\\"/subscriptions/subId/provid\
ers/Microsoft.Peering/peerAsns/myAsn1\\"}}" --peering-location "peeringLocation0" --sku name="Basic_Direct_Free" --name\
 "peeringName" --resource-group "rgName"
      - name: Create a peering with exchange route server
        text: |-
               az peering peering create --kind "Direct" --location "eastus" --direct "{\\"connections\\":[{\\"bandwidt\
hInMbps\\":10000,\\"bgpSession\\":{\\"maxPrefixesAdvertisedV4\\":1000,\\"maxPrefixesAdvertisedV6\\":100,\\"microsoftSes\
sionIPv4Address\\":\\"192.168.0.123\\",\\"peerSessionIPv4Address\\":\\"192.168.0.234\\",\\"sessionPrefixV4\\":\\"192.16\
8.0.0/24\\"},\\"connectionIdentifier\\":\\"5F4CB5C7-6B43-4444-9338-9ABC72606C16\\",\\"peeringDBFacilityId\\":99999,\\"s\
essionAddressProvider\\":\\"Peer\\",\\"useForPeeringService\\":true}],\\"directPeeringType\\":\\"IxRs\\",\\"peerAsn\\":\
{\\"id\\":\\"/subscriptions/subId/providers/Microsoft.Peering/peerAsns/myAsn1\\"}}" --peering-location "peeringLocation\
0" --sku name="Premium_Direct_Free" --name "peeringName" --resource-group "rgName"
      - name: Create an exchange peering
        text: |-
               az peering peering create --kind "Exchange" --location "eastus" --exchange "{\\"connections\\":[{\\"bgpS\
ession\\":{\\"maxPrefixesAdvertisedV4\\":1000,\\"maxPrefixesAdvertisedV6\\":100,\\"md5AuthenticationKey\\":\\"test-md5-\
auth-key\\",\\"peerSessionIPv4Address\\":\\"192.168.2.1\\",\\"peerSessionIPv6Address\\":\\"fd00::1\\"},\\"connectionIde\
ntifier\\":\\"CE495334-0E94-4E51-8164-8116D6CD284D\\",\\"peeringDBFacilityId\\":99999},{\\"bgpSession\\":{\\"maxPrefixe\
sAdvertisedV4\\":1000,\\"maxPrefixesAdvertisedV6\\":100,\\"md5AuthenticationKey\\":\\"test-md5-auth-key\\",\\"peerSessi\
onIPv4Address\\":\\"192.168.2.2\\",\\"peerSessionIPv6Address\\":\\"fd00::2\\"},\\"connectionIdentifier\\":\\"CDD8E673-C\
B07-47E6-84DE-3739F778762B\\",\\"peeringDBFacilityId\\":99999}],\\"peerAsn\\":{\\"id\\":\\"/subscriptions/subId/provide\
rs/Microsoft.Peering/peerAsns/myAsn1\\"}}" --peering-location "peeringLocation0" --sku name="Basic_Exchange_Free" --nam\
e "peeringName" --resource-group "rgName"
"""

helps['peering peering update'] = """
    type: command
    short-summary: Updates tags for a peering with the specified name under the given subscription and resource group.
    examples:
      - name: Update peering tags
        text: |-
               az peering peering update --name "peeringName" --resource-group "rgName" --tags tags={"tag0":"value0","t\
ag1":"value1"}
"""

helps['peering peering delete'] = """
    type: command
    short-summary: Deletes an existing peering with the specified name under the given subscription and resource group.
    examples:
      - name: Delete a peering
        text: |-
               az peering peering delete --name "peeringName" --resource-group "rgName"
"""

helps['peering received-route'] = """
    type: group
    short-summary: peering received-route
"""

helps['peering received-route list'] = """
    type: command
    short-summary: Lists the prefixes received over the specified peering under the given subscription and resource gro\
up.
    examples:
      - name: Lists the prefixes received over the specified peering under the given subscription and resource group.
        text: |-
               az peering received-route list --as-path "123 456" --origin-as-validation-state "Valid" --peering-name "\
peeringName" --prefix "1.1.1.0/24" --resource-group "rgName" --rpki-validation-state "Valid"
"""

helps['peering service country'] = """
    type: group
    short-summary: peering service country
"""

helps['peering service country list'] = """
    type: command
    short-summary: Lists all of the available countries for peering service.
    examples:
      - name: List peering service countries
        text: |-
               az peering service country list
"""

helps['peering service location'] = """
    type: group
    short-summary: peering service location
"""

helps['peering service location list'] = """
    type: command
    short-summary: Lists all of the available locations for peering service.
    examples:
      - name: List peering service locations
        text: |-
               az peering service location list
"""

helps['peering prefix'] = """
    type: group
    short-summary: peering prefix
"""

helps['peering prefix list'] = """
    type: command
    short-summary: Lists all prefixes under the given subscription, resource group and peering service.
    examples:
      - name: List all the prefixes associated with the peering service
        text: |-
               az peering prefix list --peering-service-name "peeringServiceName" --resource-group "rgName"
"""

helps['peering prefix show'] = """
    type: command
    short-summary: Gets an existing prefix with the specified name under the given subscription, resource group and pee\
ring service.
    examples:
      - name: Get a prefix associated with the peering service
        text: |-
               az peering prefix show --peering-service-name "peeringServiceName" --name "peeringServicePrefixName" --r\
esource-group "rgName"
"""

helps['peering prefix create'] = """
    type: command
    short-summary: Creates a new prefix with the specified name under the given subscription, resource group and peerin\
g service.
    examples:
      - name: Create or update a prefix for the peering service
        text: |-
               az peering prefix create --peering-service-name "peeringServiceName" --peering-service-prefix-key "00000\
000-0000-0000-0000-000000000000" --prefix "192.168.1.0/24" --name "peeringServicePrefixName" --resource-group "rgName"
"""

helps['peering prefix update'] = """
    type: command
    short-summary: Creates a new prefix with the specified name under the given subscription, resource group and peerin\
g service.
    examples:
      - name: Create or update a prefix for the peering service
        text: |-
               az peering prefix update --peering-service-name "peeringServiceName" --peering-service-prefix-key "00000\
000-0000-0000-0000-000000000000" --prefix "192.168.1.0/24" --name "peeringServicePrefixName" --resource-group "rgName"
"""

helps['peering prefix delete'] = """
    type: command
    short-summary: Deletes an existing prefix with the specified name under the given subscription, resource group and \
peering service.
    examples:
      - name: Delete a prefix associated with the peering service
        text: |-
               az peering prefix delete --peering-service-name "peeringServiceName" --name "peeringServicePrefixName" -\
-resource-group "rgName"
"""

helps['peering service provider'] = """
    type: group
    short-summary: peering service provider
"""

helps['peering service provider list'] = """
    type: command
    short-summary: Lists all of the available peering service locations for the specified kind of peering.
    examples:
      - name: List peering service providers
        text: |-
               az peering service provider list
"""

helps['peering service'] = """
    type: group
    short-summary: peering service
"""

helps['peering service list'] = """
    type: command
    short-summary: Lists all of the peerings under the given subscription.
    examples:
      - name: List peering services in a resource group
        text: |-
               az peering service list --resource-group "rgName"
"""

helps['peering service show'] = """
    type: command
    short-summary: Gets an existing peering service with the specified name under the given subscription and resource g\
roup.
    examples:
      - name: Get a peering service
        text: |-
               az peering service show --name "peeringServiceName" --resource-group "rgName"
"""

helps['peering service create'] = """
    type: command
    short-summary: Creates a new peering service or updates an existing peering with the specified name under the given\
 subscription and resource group.
    examples:
      - name: Create a  peering service
        text: |-
               az peering service create --location "eastus" --peering-service-location "state1" --peering-service-prov\
ider "serviceProvider1" --name "peeringServiceName" --resource-group "rgName"
"""

helps['peering service update'] = """
    type: command
    short-summary: Updates tags for a peering service with the specified name under the given subscription and resource\
 group.
    examples:
      - name: Update peering service tags
        text: |-
               az peering service update --name "peeringServiceName" --resource-group "rgName" --tags tags={"tag0":"val\
ue0","tag1":"value1"}
"""

helps['peering service delete'] = """
    type: command
    short-summary: Deletes an existing peering service with the specified name under the given subscription and resourc\
e group.
    examples:
      - name: Delete a peering service
        text: |-
               az peering service delete --name "peeringServiceName" --resource-group "rgName"
"""
