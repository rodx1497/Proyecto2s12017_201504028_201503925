<%-- 
    Document   : prueba
    Created on : 28/03/2017, 10:48:46 PM
    Author     : Rod
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <form>
        <h1>Hello World!</h1>
        <br><input type="text" name="name" /></br>
        <%
            String nombre = request.getParameter("name");
        %>
        </form>
    </body>
</html>
