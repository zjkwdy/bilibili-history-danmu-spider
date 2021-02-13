<h1>bilibili-history-danmu-spider</h1>
<hr>
<p>感谢<a href="https://github.com/SocialSisterYi/bilibili-API-collect">bilibili-API-colletc</a>
用来爬历史弹幕用的，可以整全弹幕什么的。目前支持爬取所有历史弹幕，输出标准xml格式弹幕 
使用的是B站protobuf历史弹幕接口，原因就是b站xml格式历史弹幕接口爆炸了，可以用但是返回弹幕已被关闭的信息。</p>
<h2>爬av114514(默认)</h2>
<p>食用教程：先把浏览器Cookie中的SESSDATA，例如
<code>b7723dd1%1C45141919810%2C6b33f*21</code><br>放进danmu.ini,（敲黑板奥）多个账号用英文逗号隔开
之后内容都在ini里头注释写了  </p>
<pre><code class="hljs ini"><span class="hljs-comment">;注意奥!这顺序别动，会乱的，改值就行了。（其实就是作者懒得多写）</span>
<span class="hljs-section">[account]</span>
<span class="hljs-comment">;账号相关,每个SESSDATA用英文逗号隔开，例如abcde12334232&amp;defj,kdjdhwejkh,wefioywehifh是三个</span>
<span class="hljs-attr">SESSDATA</span>=

<span class="hljs-section">[spider]</span>
<span class="hljs-comment">;爬虫设置</span>

<span class="hljs-comment">;要爬取视频的cid,可以使用getcid.py获取</span>
<span class="hljs-attr">cid</span>=<span class="hljs-number">3262388</span>

<span class="hljs-comment">;开始爬取历史弹幕的年份</span>
<span class="hljs-attr">start_year</span>=<span class="hljs-number">2011</span>
<span class="hljs-comment">;结束爬取的年份(爬取时会包含)</span>
<span class="hljs-attr">end_year</span>=<span class="hljs-number">2021</span>

<span class="hljs-comment">;每次请求前的延迟,不宜过快，会封禁IP</span>
<span class="hljs-attr">daily</span>=<span class="hljs-number">4</span>

<span class="hljs-comment">;https代理，与SESSDATA同理用英文逗号隔开，可以为空</span>
<span class="hljs-attr">proxy</span>=</code></pre>
<p>以下爬取是2021-01-01到2021-01-10 av114514全弹幕效果
<img src="https://s3.ax1x.com/2021/02/11/yBLTn1.png" alt="效果">  </p>
<h2>想要爬别的视频弹幕？</h2>
<p><strong><em>把代码中cid改成对应视频的cid即可。</em></strong></p>