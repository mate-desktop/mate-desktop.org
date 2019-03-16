/*
 * MIT License
 *
 * Copyright (c) 2017 海角在眼前
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

(function(){

    var watermark = function(self){
        this.elem = self;
    }

    watermark.prototype = {
        defaults : {
            texts : ['Watermark Text'],
            width : 100,
            height : 100,
            textRotate : -30,
            textColor : '#e5e5e5',
            textFont : '14px Sans'
        },
        options : {
            canvas : []
        },
        init : function(options){
             $.extend(this.options, this.defaults, options);
            var $body = $('body'),
                can1 = this.__createCanvas($body),
                can2 = this.__createCanvas($body),
                canAll = this.__createCanvas($body),
                settings = this.options,
                txtlen = settings.texts.length;

            settings.deg = settings.textRotate * Math.PI / 180;

            this.__calcTextSize($body);
            var repeatTimes = Math.ceil(screen.width / settings.txts.length / settings.width);
            settings.canvasWidth = settings.canvasWidth * repeatTimes;
            var extTxts = [];
            while(repeatTimes--) extTxts = extTxts.concat(settings.txts);
            settings.txts = extTxts;

            var fixH = settings.maxWidth * Math.abs(Math.sin(settings.deg)) + Math.cos(settings.deg) * settings.textHeight;
            if(fixH > settings.height) settings.height = fixH;
            var ctx1 = this.__setCanvasStyle(can1, settings.canvasWidth, settings.height);
            var ctx2 = this.__setCanvasStyle(can2, settings.canvasWidth, settings.height);
            var ctx = this.__setCanvasStyle(canAll, settings.canvasWidth, settings.height * 2, true);

            this.__drawText(ctx1, settings.txts);
            this.__drawText(ctx2, settings.txts.reverse());

            //合并canvas
            ctx.drawImage(can1, 0, 0, settings.canvasWidth, settings.height);
            ctx.drawImage(can2, 0, settings.height, settings.canvasWidth, settings.height);
            var dataURL = canAll.toDataURL("image/png");
            $(this.elem).css('backgroundImage', "url("+ dataURL +")");
            //this.__destory();
        },
        __createCanvas : function($container){
            var canvas = document.createElement('canvas');
            $container.append(canvas);
            this.options.canvas.push(canvas);
            return canvas;
        },
        __calcTextSize : function($container){
            var txts = [],
                maxWidth = 0,
                canvasWidth = 0,
                settings = this.options;
            $.each(settings.texts, function(i, text){
                var span = $('<span style="font:'+settings.textFont+';visibility: hidden;display: inline-block;"> '+text+ '</span>')
                    .appendTo($container);
                var tWidth = span[0].offsetWidth,
                    tHeight = span[0].offsetHeight;
                span.remove();
                txts.push({
                    txt : text,
                    width : tWidth,
                    height : tHeight
                });
                maxWidth = Math.max(maxWidth, tWidth);
                settings.textHeight = tHeight;
                var shadow = Math.cos(settings.deg) * tWidth;
                canvasWidth += (settings.width < shadow ? shadow : settings.width) - tHeight * Math.sin(settings.deg);
            });
            settings.txts = txts;
            settings.maxWidth = maxWidth;
            settings.canvasWidth = canvasWidth;
        },
        __setCanvasStyle : function(canvas, width, height, notextstyle){
            canvas.width = width;
            canvas.height = height;
            canvas.style.display='none';

            var ctx = canvas.getContext('2d');
            if(!notextstyle){
                var deg = this.options.deg,
                    absSindeg = Math.abs(Math.sin(deg));
                ctx.rotate(deg);
                // based on windows's x/y offset
                var offset = absSindeg * this.options.height - this.options.textHeight * absSindeg;
                var nx = - offset * Math.cos(deg),
                    ny = - offset * absSindeg;
                ctx.translate( nx, ny * absSindeg);

                ctx.font = this.options.textFont;
                ctx.fillStyle = this.options.textColor;
                ctx.textAlign = 'left';
                ctx.textBaseline = 'Middle';
            }
            return ctx;
        },
        __drawText: function(ctx, txts){
            var settings = this.options;
            $.each(txts, function(i, obj){

                var wnap = (settings.maxWidth - obj.width) / 2 ;
                var x = settings.width * Math.cos(settings.deg) * i,
                    y = - x * Math.tan(settings.deg) + settings.height;
                ctx.fillText(obj.txt, x + wnap, y);
            });
        },
        __destory : function(){
            $.each(this.options.canvas, function(i, canvas){
                canvas.remove();
                canvas = null;
            });
        }
    }

    $.fn.watermark = function(options){
        new watermark(this).init(options);
    }

})(jQuery);
