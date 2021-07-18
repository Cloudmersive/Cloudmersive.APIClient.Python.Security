# cloudmersive_security_api_client.NetworkThreatDetectionApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**network_threat_detection_detect_ssrf_url**](NetworkThreatDetectionApi.md#network_threat_detection_detect_ssrf_url) | **POST** /security/threat-detection/network/url/ssrf/detect | Check a URL for Server-side Request Forgery (SSRF) threats
[**network_threat_detection_is_bot**](NetworkThreatDetectionApi.md#network_threat_detection_is_bot) | **POST** /security/threat-detection/network/ip/is-bot | Check if IP address is a Bot client threat
[**network_threat_detection_is_threat**](NetworkThreatDetectionApi.md#network_threat_detection_is_threat) | **POST** /security/threat-detection/network/ip/is-threat | Check if IP address is a known threat
[**network_threat_detection_is_tor_node**](NetworkThreatDetectionApi.md#network_threat_detection_is_tor_node) | **POST** /security/threat-detection/network/ip/is-tor-node | Check if IP address is a Tor node server


# **network_threat_detection_detect_ssrf_url**
> UrlSsrfThreatDetectionResponseFull network_threat_detection_detect_ssrf_url(request)

Check a URL for Server-side Request Forgery (SSRF) threats

Checks if an input URL is at risk of being an SSRF (Server-side request forgery) threat or attack.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_security_api_client
from cloudmersive_security_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_security_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_security_api_client.NetworkThreatDetectionApi(cloudmersive_security_api_client.ApiClient(configuration))
request = cloudmersive_security_api_client.UrlSsrfThreatDetectionRequestFull() # UrlSsrfThreatDetectionRequestFull | Input URL request

try:
    # Check a URL for Server-side Request Forgery (SSRF) threats
    api_response = api_instance.network_threat_detection_detect_ssrf_url(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkThreatDetectionApi->network_threat_detection_detect_ssrf_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UrlSsrfThreatDetectionRequestFull**](UrlSsrfThreatDetectionRequestFull.md)| Input URL request | 

### Return type

[**UrlSsrfThreatDetectionResponseFull**](UrlSsrfThreatDetectionResponseFull.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_threat_detection_is_bot**
> ThreatDetectionBotCheckResponse network_threat_detection_is_bot(value)

Check if IP address is a Bot client threat

Check if the input IP address is a Bot, robot, or otherwise a non-user entity.  Leverages real-time signals to check against known high-probability bots..

### Example
```python
from __future__ import print_function
import time
import cloudmersive_security_api_client
from cloudmersive_security_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_security_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_security_api_client.NetworkThreatDetectionApi(cloudmersive_security_api_client.ApiClient(configuration))
value = 'value_example' # str | IP address to check, e.g. \"55.55.55.55\".  The input is a string so be sure to enclose it in double-quotes.

try:
    # Check if IP address is a Bot client threat
    api_response = api_instance.network_threat_detection_is_bot(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkThreatDetectionApi->network_threat_detection_is_bot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| IP address to check, e.g. \&quot;55.55.55.55\&quot;.  The input is a string so be sure to enclose it in double-quotes. | 

### Return type

[**ThreatDetectionBotCheckResponse**](ThreatDetectionBotCheckResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_threat_detection_is_threat**
> IPThreatDetectionResponse network_threat_detection_is_threat(value)

Check if IP address is a known threat

Check if the input IP address is a known threat IP address.  Checks against known bad IPs, botnets, compromised servers, and other lists of threats.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_security_api_client
from cloudmersive_security_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_security_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_security_api_client.NetworkThreatDetectionApi(cloudmersive_security_api_client.ApiClient(configuration))
value = 'value_example' # str | IP address to check, e.g. \"55.55.55.55\".  The input is a string so be sure to enclose it in double-quotes.

try:
    # Check if IP address is a known threat
    api_response = api_instance.network_threat_detection_is_threat(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkThreatDetectionApi->network_threat_detection_is_threat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| IP address to check, e.g. \&quot;55.55.55.55\&quot;.  The input is a string so be sure to enclose it in double-quotes. | 

### Return type

[**IPThreatDetectionResponse**](IPThreatDetectionResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **network_threat_detection_is_tor_node**
> ThreatDetectionTorNodeResponse network_threat_detection_is_tor_node(value)

Check if IP address is a Tor node server

Check if the input IP address is a Tor exit node server.  Tor servers are a type of privacy-preserving technology that can hide the original IP address who makes a request.

### Example
```python
from __future__ import print_function
import time
import cloudmersive_security_api_client
from cloudmersive_security_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_security_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_security_api_client.NetworkThreatDetectionApi(cloudmersive_security_api_client.ApiClient(configuration))
value = 'value_example' # str | IP address to check, e.g. \"55.55.55.55\".  The input is a string so be sure to enclose it in double-quotes.

try:
    # Check if IP address is a Tor node server
    api_response = api_instance.network_threat_detection_is_tor_node(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkThreatDetectionApi->network_threat_detection_is_tor_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| IP address to check, e.g. \&quot;55.55.55.55\&quot;.  The input is a string so be sure to enclose it in double-quotes. | 

### Return type

[**ThreatDetectionTorNodeResponse**](ThreatDetectionTorNodeResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

