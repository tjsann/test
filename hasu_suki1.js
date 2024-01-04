var mail = "taikoaidol6384@gmail.com";
var sei = "三浦"
var mei = "孝太"
var tell = "08056122865"

document.querySelector("#competition-application-form > fieldset:nth-child(2) > div > div > input").value=  mail;
document.querySelector("#competition-application-form > fieldset:nth-child(3) > div > div:nth-child(1) > input").value= sei;
document.querySelector("#competition-application-form > fieldset:nth-child(3) > div > div:nth-child(2) > input").value= mei;
document.querySelector("#competition-application-form > fieldset:nth-child(4) > div > div > input").value= tell
document.querySelector("#competition-application-form > fieldset:nth-child(5) > div > div > select").options[32].selected = true;
document.querySelector("#competition-application-form > fieldset:nth-child(6) > div > div > select").options[2].selected = true;
document.querySelector("#competition-application-form > fieldset:nth-child(7) > div > div > select").options[1].selected = true;
document.querySelector("#competition-application-form > fieldset:nth-child(8) > div > div > select").options[3].selected = true;
document.querySelector("#competition-application-form > fieldset:nth-child(9) > div > div > select").options[1].selected = true;
document.querySelector("#competition-application-form > fieldset:nth-child(10) > div > div > label:nth-child(4) > input").checked = true;
document.querySelector("#competition-application-form > fieldset.privacy-consent.ng-untouched.ng-pristine > label > input").checked = true;
