from flaskavel.lab.beaker.routes.router import Route

Route.middleware(['csrf']).prefix('v1').controller('HomeController').group(
    Route.get("/test/{int:id}/{string:name}", "index").name("user.index"),
)


