# StringAutomaticThreatDetection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful** | **bool** | True if the operation was successful, false otherwise | [optional] 
**clean_result** | **bool** |  | [optional] 
**contained_json_insecure_deserialization_attack** | **bool** | True if the input contained Insecure Deserialization JSON, false otherwise | [optional] 
**contained_xss_threat** | **bool** | True if the input contained XSS attack, false otherwise | [optional] 
**contained_xxe_threat** | **bool** | True if the input contained XXE attack, false otherwise | [optional] 
**contained_sql_injection_threat** | **bool** | True if the input contained SQL Injection attack, false otherwise | [optional] 
**contained_ssrf_threat** | **bool** | True if the input contained an Server-Side Request Forgery (SSRF) URL attack, false otherwise | [optional] 
**is_xml** | **bool** | True if the input string is XML, false otherwise | [optional] 
**is_json** | **bool** | True if the input string is JSON, false otherwise | [optional] 
**is_url** | **bool** | True if the input string is a URL, false otherwise | [optional] 
**original_input** | **str** | Original input string | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


