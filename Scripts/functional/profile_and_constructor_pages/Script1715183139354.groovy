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

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Log in'))

WebUI.setText(findTestObject('Object Repository/Page_QRWeb/input__username'), 'user7')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_QRWeb/input__password'), 'RigbBhfdqOALcqUsFYWzlQ==')

WebUI.click(findTestObject('Object Repository/Page_QRWeb/button_Login'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Create New Page'))

WebUI.setText(findTestObject('Object Repository/Page_QRWeb/input_Sign out_title'), 'Animals')

WebUI.verifyElementClickable(findTestObject('Object Repository/Page_QRWeb/div_CEO at Nova Solutions_owl-dot'))

WebUI.verifyElementClickable(findTestObject('Object Repository/Page_QRWeb/div_Heading'))

WebUI.verifyElementClickable(findTestObject('Object Repository/Page_QRWeb/div_List'))

WebUI.verifyElementClickable(findTestObject('Object Repository/Page_QRWeb/div_Table'))

WebUI.verifyElementClickable(findTestObject('Object Repository/Page_QRWeb/div_Image'))

WebUI.verifyElementClickable(findTestObject('Object Repository/Page_QRWeb/div_Code'))

WebUI.verifyElementClickable(findTestObject('Object Repository/Page_QRWeb/div_Link'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/button_Save page'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Open'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Back to profile'))

WebUI.verifyElementClickable(findTestObject('Object Repository/Page_QRWeb/button_Change Password'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/button_Delete'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/button_Delete Account'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Sign out'))

