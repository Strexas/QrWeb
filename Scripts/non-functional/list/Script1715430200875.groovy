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


// Define Test Object for the paragraph element
TestObject paragraphElement = findTestObject('Object Repository/Page_QRWeb/p_Experience effortless website creation wi_b8022a')

// Verify line height of unordered lists (ul)
String lineHeight = WebUI.getCSSValue(paragraphElement, 'line-height')
assert lineHeight == '27px'

// Verify bottom border of lists with the class ts-list-divided
String borderBottom = WebUI.getCSSValue(paragraphElement, 'border-bottom')
assert borderBottom == '0px none rgba(0, 0, 0, 0.5)'

// Verify padding of list items within ts-list-divided lists
String paddingTop = WebUI.getCSSValue(paragraphElement, 'padding-top')
String paddingBottom = WebUI.getCSSValue(paragraphElement, 'padding-bottom')
assert paddingTop == paddingBottom


