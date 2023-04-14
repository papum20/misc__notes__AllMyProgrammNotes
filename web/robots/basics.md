# BASICS  

  
robots.txt  
DEF :  
a file which instructs web crawlers (robots) on how to crawl your site  
LOCATION :   
must be placed in the root directory of your website, in order to be used by crawlers  
each subdomain has its own (e.g. foo.exaple.com and example.com have different files)  
ACCESS :   
	can be publicly accessed at WEBSITE.DOMAIN/robots.txt (if it has one)  
  
SYNTAX :   
separate sets of user-agent directives must be separated by a line break.  
e.g.  
	User-agent: …  
  
	User-agent: …  
Only one disallow per site can be present (for each user-agent).  
  
HOW CRAWLERS USE IT :  
when accessing a site, before indexing it: read its WEBSITE/robots.txt (if present);  
look for disallowed stuff: for each site, use the most specific pattern;  
if there are any non-disallowed link references inside: follow them (i.e. continue crawling);  
else, in other cases, stop, or follow instructions.  
note :  
Crawlers don’t always follow robots.txt instructions  
(main ones do, each in its own way).  
  
  
COMMANDS :   
User-agent: USERAGENT  
specify web crawler to give instructions to  
Disallow: URL  
	disallow crawling URL  
Disallow: \  
	disallow everything  
Disallow:  
don’t disallow anything  
Allow: URL  
	(only for google) allow, even if parent is disallowed  
Crawl-delay: MILLISECS  
	(no google) delay (ms)  
Sitemap: SITEMAP_URL  
	where to find sitemap(s)  
  
PATTERN MATCHING :   
accepts pattern matching.  
each crawler can have its own.  
common patterns :  
* : wildcard, matches any sequence  
$ : matches end of URL  
  
SOME WEB CRAWLERS :   
Bingbot : bing  
Facebot : facebook  
Googlebot : Google  
Googlebot-Image : Google images  
Slurp : Yahoo  

## README.md  
*	[README.md](./README.md)  

