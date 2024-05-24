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

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Log in'))

WebUI.setText(findTestObject('Object Repository/Page_QRWeb/input__username'), 'user7')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_QRWeb/input__password'), 'RigbBhfdqOALcqUsFYWzlQ==')

WebUI.click(findTestObject('Object Repository/Page_QRWeb/button_Login'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/a_Create New Page'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/div_CEO at Nova Solutions_owl-dot'))

WebUI.rightClick(findTestObject('Object Repository/Page_QRWeb/div_Text'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/div_Text'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/div_Table'))

WebUI.setText(findTestObject('Object Repository/Page_QRWeb/div_CEO at Nova Solutions_owl-dot'), 'f')

WebUI.setText(findTestObject('Object Repository/Page_QRWeb/div_CEO at Nova Solutions_owl-dot'), 'hhhhhhh')

WebUI.click(findTestObject('Object Repository/Page_QRWeb/svg'))

WebUI.verifyElementClickable(findTestObject('Object Repository/Page_QRWeb/svg'))

WebUI.setText(findTestObject('Object Repository/Page_QRWeb/div_CEO at Nova Solutions_owl-dot'), 'hhhh')

WebUI.setText(findTestObject('Object Repository/Page_QRWeb/div_CEO at Nova Solutions_owl-dot'), 'hhhh')

WebUI.setText(findTestObject('Object Repository/Page_QRWeb/div_CEO at Nova Solutions_owl-dot'), 'hhhhh')

WebUI.click(findTestObject('Object Repository/Page_QRWeb/svg_1'))

WebUI.verifyElementClickable(findTestObject('Object Repository/Page_QRWeb/div_Add row above'))

WebUI.verifyElementClickable(findTestObject('Object Repository/Page_QRWeb/div_Add row below'))

WebUI.verifyElementClickable(findTestObject('Object Repository/Page_QRWeb/div_Delete row'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/div_Delete row'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/svg'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/svg'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/div_With headings'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/div_Add row aboveAdd row belowDelete rowAdd_87bd6f'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/div_CEO at Nova Solutions_owl-dot'))

WebUI.setText(findTestObject('Object Repository/Page_QRWeb/div_CEO at Nova Solutions_owl-dot'), 'jhjhjb')

WebUI.click(findTestObject('Object Repository/Page_QRWeb/svg'))

WebUI.click(findTestObject('Object Repository/Page_QRWeb/svg'))

WebUI.setText(findTestObject('Object Repository/Page_QRWeb/div_CEO at Nova Solutions_owl-dot'), 'nhvjhbn')

WebUI.setText(findTestObject('Object Repository/Page_QRWeb/div_CEO at Nova Solutions_owl-dot'), 'nhvjhbn')

WebUI.setText(findTestObject('Object Repository/Page_QRWeb/div_CEO at Nova Solutions_owl-dot'), ',jb,bn ,n&nbsp;')
