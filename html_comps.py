html_header = '''
<!doctype html>
<html lang="en">
  <head>
  
      <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Jekyll v3.8.5">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.js"></script>
    </script><script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/js/bootstrap.min.js" ></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/feather-icons/4.9.0/feather.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.3/Chart.min.js"></script>

    <title>Dashboard Template · Bootstrap</title>

    
    
    <!-- Bootstrap core CSS -->
<link href="/static/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">


    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }

      <style>
#customers {
  font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid transparent;
  padding: 8px;
}
#customers th{
    border-bottom: 1px solid #ddd;
    
}


#customers tr:nth-child(even){background-color: #f2f2f2;}

#customers tr:hover {background-color: #ddd;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: rgba(0,0,0,.9);
  color: white;
}




    </style>
    <!-- Custom styles for this template -->
    <link href="/static/dashboard.css" rel="stylesheet">

  '''

def script(x):
  return'''
  <script src="/static/'''+x+'''.js"></script>
  </html>
  '''
def style(x):
  return '''
  <link href="/static/'''+x+'''.css" rel="stylesheet">
  '''
def our_table(x):
  return '<div class="table-responsive">'+x+'</div'
  
html_mid = '''

  </head>
  <body style="overflow-y: hidden;">
    <nav class="navbar navbar-dark fixed-top bg-dark flex-md-nowrap p-0 shadow">
  <a class="navbar-brand col-sm-3 col-md-2 mr-0" href="/">PESU</a>
  <input class="form-control form-control-dark w-100" type="text" placeholder="Search" aria-label="Search">
  <ul class="navbar-nav px-3">
    <li class="nav-item text-nowrap">
      <a class="nav-link" href="#">Sign out</a>
    </li>
  </ul>
</nav>

<div class="container-fluid">
  <div class="row">
    <nav id="sidebar" class="col-md-2 d-none d-md-block bg-light sidebar">
      <div class="sidebar-sticky" >
        <ul class="nav flex-column">
          <li class="nav-item">
            <a class="nav-link active" href="#">
              <span data-feather="home"></span>
              Plagiarism Scores<span class="sr-only">(current)</span>
            </a>
          </li>
          
        </ul>

        <h6 class="sidebar-heading d-flex justify-content-between align-items-center px-3 mt-4 mb-1 text-muted">
          <span>Reports & Submisions</span>
          <a class="d-flex align-items-center text-muted" href="#">
            <span data-feather="plus-circle"></span>
          </a>
        </h6>
        <ul class="nav flex-column mb-2">
          <li class="nav-item">
            <a class="nav-link" href="/">
              <span data-feather="file-text"></span>
              New Submission
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              <span data-feather="file-text"></span>
              My reports
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">
              <span data-feather="file-text"></span>
              Manage
            </a>
          </li>
        </ul>
      </div>
    </nav>

    <main role="main" class="col-md-9 ml-sm-auto col-lg-10 px-4">
      <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom" id="heading">
        <h1 class="h2">Plagiarism score table</h1>
        <div class="btn-toolbar mb-2 mb-md-0">
          <div class="btn-group mr-2">
            <button type="button" class="btn btn-sm btn-outline-secondary">Share</button>
            <button type="button" class="btn btn-sm btn-outline-secondary">Export</button>
          </div>
          <button type="button" class="btn btn-sm btn-outline-secondary dropdown-toggle">
            <span data-feather="calendar"></span>
            This week
          </button>
        </div>
      </div>
<br>
<br>
 
'''

html_login = '''
  <form id="login_form" class="form-signin">
  <img class="mb-4" src="/docs/4.3/assets/brand/bootstrap-solid.svg" alt="" width="72" height="72">
  <center><h1 class="h3 mb-3 font-weight-normal">Please sign in</h1></center>
  <label for="inputEmail" class="sr-only">Email address</label>
  <input type="" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
  <label for="inputPassword" class="sr-only">Password</label>
  <input type="password" id="inputPassword" class="form-control" placeholder="Password" required>
  <div class="checkbox mb-3">
    <label>
      <input type="checkbox" value="remember-me"> Remember me
    </label>
  </div>
  <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
  <br>
  <div class="alert alert-warning" id ="fail" role="alert">
      Login Failed
  </div>
  <p class="mt-5 mb-3 text-muted">&copy; 2017-2019</p>
</form>
'''

html_footer ='''

    </main>
  </div>
</div>
'''


html_admin_page = '''
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        Pakka u wnna remove?
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" id="paramsOkay" class="btn btn-primary">Confirm</button>
      </div>
    </div>
  </div>
</div>
<div id="ModalExample" class="modal fade" style="font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;font-weight: lighter" >
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h4 class="modal-title " style="font-weight: lighter">Enter your details</h4>
            </div>
            <div class="modal-body">
                <form id="start_form">
                    <div class="form-group">
                        <label for="exampleInputPassword1">Username</label>
                        <input type="text" class="form-control" id="new_name" placeholder="Enter your username">
                      </div>
                    <div class="form-group">
                      <label for="exampleInputEmail1">Email address</label>
                      <input type="email" class="form-control" id="new_mail" aria-describedby="emailHelp" placeholder="Enter email">
                      <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
                    </div>
                   
                  
                      
                   <br>
                    <button id="add_mem"  class="btn btn-primary float-right"  >Submit</button>
                    <button type="reset" class="btn btn-secondary" >Reset</button>
                  </form>
            </div>
            <div  class="modal-footer float-left" >
              <span id="formmsg" style="position: relative;right:20%">
                           </span></div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div><!-- /.modal -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<main role="main" id="manager" class="container">
  <div class="d-flex align-items-center p-3 my-3 text-white-50 bg-purple rounded shadow-sm">
    <img class="mr-3" src="/docs/4.3/assets/brand/bootstrap-outline.svg" alt="" width="48" height="48">
    <div class="lh-100">
      <h4 class="mb-0 text-white lh-100">Manage Members</h4>
      <small>PESU Scams</small>
    </div>
  </div>

  <div id="mycontent" class="my-3 p-3 bg-white rounded shadow-sm">
  
  </div>
  
</main>
'''


html_home_page = '''
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        Pakka u wnna remove?
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" id="paramsOkay" class="btn btn-primary">Confirm</button>
      </div>
    </div>
  </div>
</div>
<div id="ModalExample" class="modal fade" style="font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;font-weight: lighter" >
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h4 class="modal-title " style="font-weight: lighter">Enter your details</h4>
            </div>
            <div class="modal-body">
                <form id="start_form">
                    <div class="form-group">
                        <label for="exampleInputPassword1">Username</label>
                        <input type="text" class="form-control" id="course_id" placeholder="Enter Course ID">
                      </div>
                  
                      
                   <br>
                    <button id="add_course"  class="btn btn-primary float-right"  >Submit</button>
                    <button type="reset" class="btn btn-secondary" >Reset</button>
                  </form>
            </div>
            <div  class="modal-footer float-left" >
              <span id="formmsg" style="position: relative;right:20%">
                           </span></div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div><!-- /.modal -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<main role="main" id="manager" class="container">
  <div class="d-flex align-items-center p-3 my-3 text-white-50 bg-purple rounded shadow-sm">
    <img class="mr-3" src="/docs/4.3/assets/brand/bootstrap-outline.svg" alt="" width="48" height="48">
    <div class="lh-100">
      <h4 class="mb-0 text-white lh-100">My Courses</h4>
      <small>PESU Scams</small>
    </div>
  </div>

  <div id="mycontent" class="my-3 p-3 bg-white rounded shadow-sm">
  
  </div>
  
</main>
'''
html_ass_page  = '''
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        Pakka u wnna remove?
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" id="paramsOkay" class="btn btn-primary">Confirm</button>
      </div>
    </div>
  </div>
</div>
<div id="ModalExample" class="modal fade" style="font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;font-weight: lighter" >
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h4 class="modal-title " style="font-weight: lighter">Enter your details</h4>
            </div>
            <div class="modal-body">
                <form id="start_form">
                    <div class="form-group">
                        <label for="exampleInputPassword1">Username</label>
                        <input type="text" class="form-control" id="new_name" placeholder="Enter your username">
                      </div>
                    <div class="form-group">
                      <label for="exampleInputEmail1">Email address</label>
                      <input type="email" class="form-control" id="new_mail" aria-describedby="emailHelp" placeholder="Enter email">
                      <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
                    </div>
                   
                  
                      
                   <br>
                    <button id="add_mem"  class="btn btn-primary float-right"  >Submit</button>
                    <button type="reset" class="btn btn-secondary" >Reset</button>
                  </form>
            </div>
            <div  class="modal-footer float-left" >
              <span id="formmsg" style="position: relative;right:20%">
                           </span></div>
        </div><!-- /.modal-content -->
    </div><!-- /.modal-dialog -->
</div><!-- /.modal -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<main role="main" id="manager" class="container">
  <div class="d-flex align-items-center p-3 my-3 text-white-50 bg-purple rounded shadow-sm" style="background-color:#bf3d2e">
    <img class="mr-3" src="/docs/4.3/assets/brand/bootstrap-outline.svg" alt="" width="48" height="48">
    <div class="lh-100">
      <h4 class="mb-0 text-white lh-100">Manage Assignments</h4>
      <small>PESU Scams</small>
    </div>
  </div>

  <div id="mycontent" class="my-3 p-3 bg-white rounded shadow-sm">
  
  </div>
  
</main>
'''