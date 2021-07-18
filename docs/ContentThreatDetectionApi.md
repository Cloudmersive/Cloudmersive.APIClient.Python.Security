# cloudmersive_security_api_client.ContentThreatDetectionApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_threat_detection_automatic_threat_detection_string**](ContentThreatDetectionApi.md#content_threat_detection_automatic_threat_detection_string) | **POST** /security/threat-detection/content/automatic/detect/string | Automatically detect threats in an input string
[**content_threat_detection_check_sql_injection_string**](ContentThreatDetectionApi.md#content_threat_detection_check_sql_injection_string) | **POST** /security/threat-detection/content/sql-injection/detect/string | Check text input for SQL Injection (SQLI) attacks
[**content_threat_detection_check_xxe**](ContentThreatDetectionApi.md#content_threat_detection_check_xxe) | **POST** /security/threat-detection/content/xxe/detect/xml/string | Protect text input from XML External Entity (XXE) attacks
[**content_threat_detection_detect_insecure_deserialization_json_string**](ContentThreatDetectionApi.md#content_threat_detection_detect_insecure_deserialization_json_string) | **POST** /security/threat-detection/content/insecure-deserialization/json/detect/string | Detect Insecure Deserialization JSON (JID) attacks in a string
[**content_threat_detection_protect_xss**](ContentThreatDetectionApi.md#content_threat_detection_protect_xss) | **POST** /security/threat-detection/content/xss/detect/string | Protect text input from Cross-Site-Scripting (XSS) attacks through normalization


# **content_threat_detection_automatic_threat_detection_string**
> StringAutomaticThreatDetection content_threat_detection_automatic_threat_detection_string(value)

Automatically detect threats in an input string

Auto-detects a wide range of threat types in input string, including Cross-Site Scripting (XSS), SQL Injection (SQLI), XML External Entitites (XXE), Server-side Request Forgeries (SSRF), and JSON Insecure Deserialization (JID).

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
api_instance = cloudmersive_security_api_client.ContentThreatDetectionApi(cloudmersive_security_api_client.ApiClient(configuration))
value = 'value_example' # str | User-facing text input.

try:
    # Automatically detect threats in an input string
    api_response = api_instance.content_threat_detection_automatic_threat_detection_string(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentThreatDetectionApi->content_threat_detection_automatic_threat_detection_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| User-facing text input. | 

### Return type

[**StringAutomaticThreatDetection**](StringAutomaticThreatDetection.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_threat_detection_check_sql_injection_string**
> StringSqlInjectionDetectionResult content_threat_detection_check_sql_injection_string(value)

Check text input for SQL Injection (SQLI) attacks

Detects SQL Injection (SQLI) attacks from text input.

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
api_instance = cloudmersive_security_api_client.ContentThreatDetectionApi(cloudmersive_security_api_client.ApiClient(configuration))
value = 'value_example' # str | User-facing text input.

try:
    # Check text input for SQL Injection (SQLI) attacks
    api_response = api_instance.content_threat_detection_check_sql_injection_string(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentThreatDetectionApi->content_threat_detection_check_sql_injection_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| User-facing text input. | 

### Return type

[**StringSqlInjectionDetectionResult**](StringSqlInjectionDetectionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_threat_detection_check_xxe**
> StringXxeDetectionResult content_threat_detection_check_xxe(value)

Protect text input from XML External Entity (XXE) attacks

Detects XXE (XML External Entity) attacks from XML text input.

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
api_instance = cloudmersive_security_api_client.ContentThreatDetectionApi(cloudmersive_security_api_client.ApiClient(configuration))
value = 'value_example' # str | User-facing text input.

try:
    # Protect text input from XML External Entity (XXE) attacks
    api_response = api_instance.content_threat_detection_check_xxe(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentThreatDetectionApi->content_threat_detection_check_xxe: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| User-facing text input. | 

### Return type

[**StringXxeDetectionResult**](StringXxeDetectionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_threat_detection_detect_insecure_deserialization_json_string**
> StringInsecureDeserializationJsonDetection content_threat_detection_detect_insecure_deserialization_json_string(value)

Detect Insecure Deserialization JSON (JID) attacks in a string

Detects Insecure Deserialization JSON (JID) attacks from text input.

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
api_instance = cloudmersive_security_api_client.ContentThreatDetectionApi(cloudmersive_security_api_client.ApiClient(configuration))
value = 'value_example' # str | User-facing text input.

try:
    # Detect Insecure Deserialization JSON (JID) attacks in a string
    api_response = api_instance.content_threat_detection_detect_insecure_deserialization_json_string(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentThreatDetectionApi->content_threat_detection_detect_insecure_deserialization_json_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| User-facing text input. | 

### Return type

[**StringInsecureDeserializationJsonDetection**](StringInsecureDeserializationJsonDetection.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **content_threat_detection_protect_xss**
> StringXssProtectionResult content_threat_detection_protect_xss(value)

Protect text input from Cross-Site-Scripting (XSS) attacks through normalization

Detects and removes XSS (Cross-Site-Scripting) attacks from text input through normalization.  Returns the normalized result, as well as information on whether the original input contained an XSS risk.

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
api_instance = cloudmersive_security_api_client.ContentThreatDetectionApi(cloudmersive_security_api_client.ApiClient(configuration))
value = 'value_example' # str | User-facing text input.

try:
    # Protect text input from Cross-Site-Scripting (XSS) attacks through normalization
    api_response = api_instance.content_threat_detection_protect_xss(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContentThreatDetectionApi->content_threat_detection_protect_xss: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**| User-facing text input. | 

### Return type

[**StringXssProtectionResult**](StringXssProtectionResult.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

