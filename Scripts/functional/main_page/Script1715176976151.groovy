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

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Home (current)'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Learn More'))

WebUI.verifyElementText(findTestObject('Object Repository/Page_QRWeb/h2_How It Works'), 'How It Works')

WebUI.verifyElementText(findTestObject('Object Repository/Page_QRWeb/h4_Create Your Page'), 'Create Your Page')

WebUI.verifyElementText(findTestObject('Object Repository/Page_QRWeb/h4_Link It To QR'), 'Link It To QR')

WebUI.verifyElementText(findTestObject('Object Repository/Page_QRWeb/h4_Share It'), 'Share It')

WebUI.verifyElementText(findTestObject('Object Repository/Page_QRWeb/p_Effortlessly share your fantastic page wi_fa3955'), 
    'Effortlessly share your fantastic page with friends, colleagues, and the world, and let your creativity shine!')

WebUI.verifyElementVisible(findTestObject('Object Repository/Page_QRWeb/p_Easily connect your page to a QR code, si_cf769b'), 
    FailureHandling.STOP_ON_FAILURE)

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_About'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Sign Up Now'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Login_navbar-brand'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Contact'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/h3_Contact Us'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/figure_Student g. 50, Kaunas, Lithuania'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_About'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/h2_What Is QRWeb'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Log in'))

