# cloudmersive_security_api_client
The security APIs help you detect and block security threats.

This Python package provides a native API client for [Cloudmersive Security Threat Detection API](https://www.cloudmersive.com/security-threat-detection-api)

- API version: v1
- Package version: 3.0.1
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cloudmersive_security_api_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cloudmersive_security_api_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ContentThreatDetectionApi* | [**content_threat_detection_automatic_threat_detection_string**](docs/ContentThreatDetectionApi.md#content_threat_detection_automatic_threat_detection_string) | **POST** /security/threat-detection/content/automatic/detect/string | Automatically detect threats in an input string
*ContentThreatDetectionApi* | [**content_threat_detection_check_sql_injection_string**](docs/ContentThreatDetectionApi.md#content_threat_detection_check_sql_injection_string) | **POST** /security/threat-detection/content/sql-injection/detect/string | Check text input for SQL Injection (SQLI) attacks
*ContentThreatDetectionApi* | [**content_threat_detection_check_xxe**](docs/ContentThreatDetectionApi.md#content_threat_detection_check_xxe) | **POST** /security/threat-detection/content/xxe/detect/xml/string | Protect text input from XML External Entity (XXE) attacks
*ContentThreatDetectionApi* | [**content_threat_detection_detect_insecure_deserialization_json_string**](docs/ContentThreatDetectionApi.md#content_threat_detection_detect_insecure_deserialization_json_string) | **POST** /security/threat-detection/content/insecure-deserialization/json/detect/string | Detect Insecure Deserialization JSON (JID) attacks in a string
*ContentThreatDetectionApi* | [**content_threat_detection_protect_xss**](docs/ContentThreatDetectionApi.md#content_threat_detection_protect_xss) | **POST** /security/threat-detection/content/xss/detect/string | Protect text input from Cross-Site-Scripting (XSS) attacks through normalization
*NetworkThreatDetectionApi* | [**network_threat_detection_detect_ssrf_url**](docs/NetworkThreatDetectionApi.md#network_threat_detection_detect_ssrf_url) | **POST** /security/threat-detection/network/url/ssrf/detect | Check a URL for Server-side Request Forgery (SSRF) threats
*NetworkThreatDetectionApi* | [**network_threat_detection_is_bot**](docs/NetworkThreatDetectionApi.md#network_threat_detection_is_bot) | **POST** /security/threat-detection/network/ip/is-bot | Check if IP address is a Bot client threat
*NetworkThreatDetectionApi* | [**network_threat_detection_is_threat**](docs/NetworkThreatDetectionApi.md#network_threat_detection_is_threat) | **POST** /security/threat-detection/network/ip/is-threat | Check if IP address is a known threat
*NetworkThreatDetectionApi* | [**network_threat_detection_is_tor_node**](docs/NetworkThreatDetectionApi.md#network_threat_detection_is_tor_node) | **POST** /security/threat-detection/network/ip/is-tor-node | Check if IP address is a Tor node server


## Documentation For Models

 - [IPThreatDetectionResponse](docs/IPThreatDetectionResponse.md)
 - [StringAutomaticThreatDetection](docs/StringAutomaticThreatDetection.md)
 - [StringInsecureDeserializationJsonDetection](docs/StringInsecureDeserializationJsonDetection.md)
 - [StringSqlInjectionDetectionResult](docs/StringSqlInjectionDetectionResult.md)
 - [StringXssProtectionResult](docs/StringXssProtectionResult.md)
 - [StringXxeDetectionResult](docs/StringXxeDetectionResult.md)
 - [ThreatDetectionBotCheckResponse](docs/ThreatDetectionBotCheckResponse.md)
 - [ThreatDetectionTorNodeResponse](docs/ThreatDetectionTorNodeResponse.md)
 - [UrlSsrfThreatDetectionRequestFull](docs/UrlSsrfThreatDetectionRequestFull.md)
 - [UrlSsrfThreatDetectionResponseFull](docs/UrlSsrfThreatDetectionResponseFull.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



