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
WebUI.navigateToUrl('https://qr-web-h1fi.onrender.com/')

// Define Test Object for the body element
TestObject bodyElement = findTestObject('Object Repository/Page_QRWeb/p_QRWeb offers a hassle-free solution for w_42d83d')

WebUI.getCSSValue(bodyElement, 'color')

// Verify font family of the body text
String fontFamily = WebUI.getCSSValue(bodyElement, 'font-family')
assert fontFamily.contains("Poppins") || fontFamily.contains("sans-serif")

// Verify font weight of the body text
String fontWeight = WebUI.getCSSValue(bodyElement, 'font-weight')
assert fontWeight == '400'

// Convert font size from px to rem (assuming 1rem = 16px)
def expectedFontSizeRem = 14.25 / 16

// Verify font size of the body text
String fontSize = WebUI.getCSSValue(bodyElement, 'font-size')

// Convert font size from px to rem for comparison
def actualFontSizeRem = fontSize.replace("px", "").toBigDecimal() / 16

// Assert font size in rem
assert actualFontSizeRem == expectedFontSizeRem