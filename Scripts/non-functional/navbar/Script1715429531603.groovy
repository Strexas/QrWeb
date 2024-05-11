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

// Define Test Object for the navbar element
TestObject navbarElement = findTestObject('Object Repository/Page_QRWeb/a_About')

// Verify font size and font weight of navbar links
String fontSize = WebUI.getCSSValue(navbarElement, 'font-size')
String fontWeight = WebUI.getCSSValue(navbarElement, 'font-weight')
assert fontSize == '13.3px' && fontWeight == '500'

// Verify padding of navbar
String paddingTop = WebUI.getCSSValue(navbarElement, 'padding-top')
String paddingBottom = WebUI.getCSSValue(navbarElement, 'padding-bottom')
assert paddingTop == '4.75px'
assert paddingBottom == '4.75px'

// Verify smooth transition for background color
String transition = WebUI.getCSSValue(navbarElement, 'transition')
assert transition == 'all 0.3s ease 0s'

