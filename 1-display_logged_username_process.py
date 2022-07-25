

"""
STEP 1 :
file: website/main/templates/main/base.html
# This is the master html file that will define the layout
# of all later pages.
*************************************************************
"""
# ...
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <div>
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a href="/home" class="nav-link">Home</a>
                    </li>
                    <li class="nav-item">
                        <a href="/create-post" class="nav-link">Post</a>
                    </li>
                </ul>
            </div>
            <div>
                <ul class="navbar-nav">
                    {% if user.is_authenticated %}
                    # Logged User username
                    <span class="navbar-text">Logged in as {{user.username}}  | </span>
                    <li class="nav-item">
                        <a href="/logout" class="nav-link">Logout</a>
                    </li>

                    {% else %}

                    <li class="nav-item">
                        <a href="/login" class="nav-link">Login</a>
                    </li>

                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>
# ...