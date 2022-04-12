Tutorial：

打开浏览器控制台（F12）--> 选择`sources` --> `snippet`:

``` javascript
var x=5,y=10;
    function autoClick()
    {
        y=y+5;
        var zan=document.getElementsByClassName('item qz_like_btn_v3');
        for(var i=0;i<zan.length;i++){
            if(zan[i].attributes[6].value=='like'){
                zan[i].firstChild.click();
            }
        };
        window.scrollBy(x,y);
    }
 
    window.setInterval(autoClick,2000);
```