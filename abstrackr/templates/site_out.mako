<%def name="title()"></%def>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <link rel="stylesheet" href="/stylesheet.css">
        <script type="text/javascript" src="/scripts/jquery-1.4.4.js"></script>
        <script type="text/javascript" src="/scripts/CalendarPopup.js"></script>
        <title>abstrackr: ${self.title()}</title>
    </head>
    <body>
        <div style="background-color: #ffebee; border: 1px solid #ef9a9a; padding: 15px; margin: 50px 20px 0 20px; text-align: center;">
            <p style="font-size: 16px; color: #b71c1c; margin: 0;">
                <strong>Important Notice:</strong> We are actively working on improving Abstrackr's performance and responsiveness. 
                However, if you're looking for a more up-to-date abstract screening tool with machine learning assistance that is actively in development and receives full support, 
                we recommend visiting <a href="https://srdrplus.ahrq.gov/" style="color: #0d47a1;">https://srdrplus.ahrq.gov/</a>.
            </p>
        </div>

        <p align="left">
        <img src = "../../abstrackr.png"></img>
        </p>
       
	
<!-- *** BEGIN page content *** -->
${self.body()}
<!-- *** END page content *** -->

    </body>
</html>
