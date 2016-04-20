# python-xss-filter
Based on native Python module HTMLParser purifier of HTML, To Clear all javascript in html  

## Python 富文本XSS过滤类
@ phith0n的python-xss-filter修改版
@ 原作者link: https://github.com/phith0n/python-xss-filter  

## Usage:
    
        import pxfilter
        parser = pxfilter.XssHtml()
        parser.feed('<html code>')
        parser.close()
        html = parser.getHtml()
        print html


### Requirements
Python 2.6+ or 3.2+  
浏览器版本：IE7+ 或其他浏览器，无法防御IE6及以下版本浏览器中的XSS  
