package org.cloudothon.tests;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.htmlunit.HtmlUnitDriver;
import org.openqa.selenium.remote.BrowserType;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;



public class BookTests {

	public static WebDriver driver;
	
	public static String baseUrl="http://18.202.212.88/";
	
	public static String userNameText="//input[@name='username']";
	
	public static String passwordText="//input[@name='username']";
	
	public static String loginButton="//*[@type='submit']";
	
	@BeforeTest
	public void setBaseUrl(){
		
		DesiredCapabilities cap=new DesiredCapabilities();
		cap.setBrowserName(BrowserType.FIREFOX);
		try {
			driver =new RemoteWebDriver(new URL("http://54.165.40.107"),cap);
		} catch (MalformedURLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		driver.get(baseUrl);
		//System.setProperty("webdriver.chrome.driver","C:\\chromedriver\\chromedriver.exe");
		//driver = new ChromeDriver();
		//WebDriver driver = new HtmlUnitDriver(true);
		driver.manage().timeouts().pageLoadTimeout(40, TimeUnit.SECONDS);
		driver.get(baseUrl);
	}
	
	@Test
	public void verifyLogin(){
		
		driver.findElement(By.xpath(userNameText)).sendKeys("asd");
		driver.findElement(By.xpath(passwordText)).sendKeys("asd");
		driver.findElement(By.xpath(loginButton)).submit();
		driver.quit();
		
	}
	
	
	

	
	
}
