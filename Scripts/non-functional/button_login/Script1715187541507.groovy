import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.maximizeWindow()

WebUI.navigateToUrl('https://qr-web-h1fi.onrender.com/')

WebUI.getCSSValue(findTestObject('Object Repository/Page_QRWeb/a_Log in'), 'color')

WebUI.getCSSValue(findTestObject('Object Repository/Page_QRWeb/a_Log in'), 'font-family')

WebUI.getCSSValue(findTestObject('Object Repository/Page_QRWeb/a_Log in'), 'background-color')

height = WebUI.getElementHeight(findTestObject('Object Repository/Page_QRWeb/a_Log in'))

width = WebUI.getElementWidth(findTestObject('Object Repository/Page_QRWeb/a_Log in'))

WebUI.getCSSValue(findTestObject('Object Repository/Page_QRWeb/a_Log in'), 'color')

// Define Test Object for the button element
TestObject buttonElement = findTestObject('Object Repository/Page_QRWeb/a_Log in')

// Verify border radius of the button
String borderRadius = WebUI.getCSSValue(buttonElement, 'border-radius')

assert borderRadius == '100px' //6.25rem*16px

// Verify font weight of button text
String fontWeight = WebUI.getCSSValue(buttonElement, 'font-weight')

assert fontWeight == '600'

// Verify font size of button text
String fontSizeRem = WebUI.getCSSValue(buttonElement, 'font-size')

assert fontSizeRem == '13px' // 0.9375rem * 16px = 15px

// Verify padding of button
// Verify padding of button
String paddingVertical = WebUI.getCSSValue(buttonElement, 'padding-top')

String paddingHorizontal = WebUI.getCSSValue(buttonElement, 'padding-right')

assert (paddingVertical == '5px') && (paddingHorizontal == '16px')

// Verify box shadow of button
String boxShadow = WebUI.getCSSValue(buttonElement, 'box-shadow')

assert boxShadow == 'rgba(0, 0, 0, 0.15) 2px 3px 15px 0px'

// Verify status indicator height and width
String statusIndicatorHeight = WebUI.getCSSValue(buttonElement, 'height')

String statusIndicatorWidth = WebUI.getCSSValue(buttonElement, 'width')

assert (statusIndicatorHeight == '32.7px') && (statusIndicatorWidth == '73.5875px')

// Verify status icon border radius, font size, and padding
String statusIconBorderRadius = WebUI.getCSSValue(buttonElement, 'border-radius')

String statusIconFontSize = WebUI.getCSSValue(buttonElement, 'font-size')

String statusIconPaddingVertical = WebUI.getCSSValue(buttonElement, 'padding-top')

String statusIconPaddingHorizontal = WebUI.getCSSValue(buttonElement, 'padding-right')

assert (((statusIconBorderRadius == '100px') && (statusIconFontSize == '13px')) && (statusIconPaddingVertical == '5px')) && 
(statusIconPaddingHorizontal == '16px')

// Verify background color, border color, and text color of primary button
String backgroundColor = WebUI.getCSSValue(buttonElement, 'background-color')

String borderColor = WebUI.getCSSValue(buttonElement, 'border-color')

String textColor = WebUI.getCSSValue(buttonElement, 'color')

assert ((backgroundColor == 'rgba(56, 131, 200, 1)') && (borderColor == 'rgb(56, 131, 200)')) && (textColor == 'rgba(255, 255, 255, 1)')


