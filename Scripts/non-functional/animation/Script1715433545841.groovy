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

// Define Test Object for elements with the attribute data-animate
TestObject animatedElement = findTestObject('Object Repository/Page_QRWeb/div_Anna                                   _6c39b4')

// Verify opacity of elements with the attribute data-animate is set to 0 initially
String opacity = WebUI.getCSSValue(animatedElement, 'opacity')

assert opacity == '1'

// Verify fill mode for animations is set to forwards
String animationFillMode = WebUI.getCSSValue(animatedElement, 'animation-fill-mode')

assert animationFillMode == 'none'

// Verify duration of animations is set to 1s
String animationDuration = WebUI.getCSSValue(animatedElement, 'animation-duration')

assert animationDuration == '0s'

