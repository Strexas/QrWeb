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

WebUI.navigateToUrl('http://127.0.0.1:8000/#page-top')

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Home (current)'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Learn More'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_About'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Pricing'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Contact'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/h3_Contact Us'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/figure_Student g. 50, Kaunas, Lithuania'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_About'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/h2_What Is QRWeb'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Pricing'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/h2_Affordable Prices'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/h2_Our Clients'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/h2_Our Team'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Log in'))

