'use strict'

var creative = {

  // config
  container: null,

  layer1: null,
  layer2: null,
  layer3: null,

  text1: null,
  text2: null,
  text3: null,
  cta:null,

  bgExit: null,

  bg1:'',
  bg2:'',
  bg3:'',

  text1Content: '',
  text2Content: '',
  text3Content: '',
  text1Size: 20,
  text2Size: 20,
  text3Size: 20,
  ctaContent: '',
  ctaSize: 16,

  fontname: '',
  font: '',

  exitURL:'',

  init: function() {

    // DYNAMIC CONTENT
    Enabler.setProfileId(10058413);
    var devDynamicContent = {};

    devDynamicContent.Dynamic_Ads_June_2018_Feed= [{}];
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0]._id = 0;
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Unique_ID = 1;
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Reporting_Label = "Canada_300x600";
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Ad_Name = "";
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Weights = 50;
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].fontname = "";
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].AssetLibrary_Font = {"NotoSansSC-Bold.otf":{"Type":"file","Url":"https://s0.2mdn.net/ads/richmedia/studio/28384/28384_20180619022855401_NotoSansSC-Bold.otf"},"NotoSansJP-Bold.otf":{"Type":"file","Url":"https://s0.2mdn.net/ads/richmedia/studio/28384/28384_20180619022835335_NotoSansJP-Bold.otf"},"ISTKMaquette-Bold.otf":{"Type":"file","Url":"https://s0.2mdn.net/ads/richmedia/studio/pv2/66274049/dirty/ISTKMaquette-Bold.otf"}};
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Text_1 = "Make Your Creative Stand Out";
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Text_1_Size = 45;
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].AssetLibrary_1 = {};
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].AssetLibrary_1.Type = "file";
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].AssetLibrary_1.Url = "https://s0.2mdn.net/ads/richmedia/studio/28384/28384_20180405022206679_IS_Digital_Template_300x600_Frame1.jpg";
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Text_2 = "Lower Price, Higher Quality";
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Text_2_Size = 45;
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].AssetLibrary_2 = {};
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].AssetLibrary_2.Type = "file";
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].AssetLibrary_2.Url = "https://s0.2mdn.net/ads/richmedia/studio/28384/28384_20180405022219664_IS_Digital_Template_300x600_Frame2.jpg";
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Text_3 = "Stock That Makes an Impact";
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Text_3_Size = 45;
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].AssetLibrary_3 = {};
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].AssetLibrary_3.Type = "file";
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].AssetLibrary_3.Url = "https://s0.2mdn.net/ads/richmedia/studio/28384/28384_20180405022230561_IS_Digital_Template_300x600_Frame3.jpg";
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].CTA = "Explore Now";
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].CTA_Text_Size = 20;
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Default = false;
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Active = true;
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Exit_URL = {};
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Exit_URL.Url = "https://www.psycle.com/";
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Backup_Image = {};
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Backup_Image.Type = "file";
    devDynamicContent.Dynamic_Ads_June_2018_Feed[0].Backup_Image.Url = "https://s0.2mdn.net/ads/richmedia/studio/28384/28384_20180412014307828_IS_Digital_Template_300x600_Backup.jpg";
    Enabler.setDevDynamicContent(devDynamicContent);

    creative.setupDom();

    creative.bg1 = dynamicContent.Dynamic_Ads_June_2018_Feed[0].AssetLibrary_1.Url;
    creative.bg2 = dynamicContent.Dynamic_Ads_June_2018_Feed[0].AssetLibrary_2.Url;
    creative.bg3 = dynamicContent.Dynamic_Ads_June_2018_Feed[0].AssetLibrary_3.Url;

    creative.text1Content = dynamicContent.Dynamic_Ads_June_2018_Feed[0].Text_1;
    creative.text2Content = dynamicContent.Dynamic_Ads_June_2018_Feed[0].Text_2;
    creative.text3Content = dynamicContent.Dynamic_Ads_June_2018_Feed[0].Text_3;
    creative.text1Size = dynamicContent.Dynamic_Ads_June_2018_Feed[0].Text_2_Size;
    creative.text2Size = dynamicContent.Dynamic_Ads_June_2018_Feed[0].Text_2_Size;
    creative.text3Size = dynamicContent.Dynamic_Ads_June_2018_Feed[0].Text_3_Size;

    creative.ctaContent = dynamicContent.Dynamic_Ads_June_2018_Feed[0].CTA;
    creative.ctaSize = dynamicContent.Dynamic_Ads_June_2018_Feed[0].CTA_Text_Size;

    creative.exitURL = dynamicContent.Dynamic_Ads_June_2018_Feed[0].Exit_URL.Url;

    // setup font
    creative.fontname = dynamicContent.Dynamic_Ads_June_2018_Feed[0].fontname;
    if (creative.fontname === '') {
      creative.fontname = 'ISTKMaquette-Bold';
    }
    creative.font = dynamicContent.Dynamic_Ads_June_2018_Feed[0].AssetLibrary_Font[creative.fontname + '.otf'].Url;

    var styleEl = document.createElement('style');
    document.head.appendChild(styleEl);
    styleEl.appendChild(document.createTextNode(''));
    var sheet = styleEl.sheet;
    sheet.insertRule("@font-face { font-family: '" + creative.fontname + "'; src: url('" + creative.font + "') format('opentype'); }", 0);
    sheet.insertRule("body, body * { font-family: '" + creative.fontname + "', Arial, sans-serif; }", 1);

    creative.addListeners();

    // Polite loading
    if(Enabler.isPageLoaded()) {
      creative.setup();
    } else {
      Enabler.addEventListener(studio.events.StudioEvent.PAGE_LOADED, creative.setup);
    }

    if (Enabler.isVisible()) {
      creative.show();
    }
    else {
      Enabler.addEventListener(studio.events.StudioEvent.VISIBLE, creative.show);
    }
  },

  setupDom: function() {

    // get DOM elements
    creative.container=document.getElementById('container');

    creative.layer1=document.getElementById('background1');
    creative.layer2=document.getElementById('background2');
    creative.layer3=document.getElementById('background3');

    creative.text1=document.getElementById('text1');
    creative.text2=document.getElementById('text2');
    creative.text3=document.getElementById('text3');

    creative.cta=document.getElementById('cta');

    creative.bgExit=document.getElementById('bg-exit');
  },

  addListeners: function() {
    creative.bgExit.addEventListener('click', creative.exitClickHandler);
  },

  exitClickHandler: function() {
    if (creative.exitURL=='') {
      Enabler.exit('Background Exit');
    } else {
      Enabler.exitOverride('Background Exit', creative.exitURL);
    }

  },

  setup: function() {
    //console.log('setup');

    creative.layer1.style.backgroundImage='url("'+creative.bg1+'")';
    creative.layer2.style.backgroundImage='url("'+creative.bg2+'")';
    creative.layer3.style.backgroundImage='url("'+creative.bg3+'")';

    creative.text1.innerHTML=creative.text1Content;
    creative.text2.innerHTML=creative.text2Content;
    creative.text3.innerHTML=creative.text3Content;
    creative.text1.style.fontSize=creative.text1Size+'px';
    creative.text2.style.fontSize=creative.text2Size+'px';
    creative.text3.style.fontSize=creative.text3Size+'px';
    creative.cta.innerHTML=creative.ctaContent;
    creative.cta.style.fontSize=creative.ctaSize+'px';

    creative.container.classList.add('show');
  },
  show: function() {
    //console.log('init');
  }
}


// If true, start function. If false, listen for INIT.
window.onload = function() {
  if (Enabler.isInitialized()) {
      creative.init();
  } else {
      Enabler.addEventListener(studio.events.StudioEvent.INIT, creative.init);
  }
}