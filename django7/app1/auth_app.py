#Type of Auth
#Basic Auth > send the authentication credentials with every request
# Pros > simple
# Cons > credentials are sent with every request, which can be a security risk if not using HTTPS

# Token Auth > server generates a random string called token and sends it to the client, which stores it and sends it with every request
# pros > easy to use apis
# cons > token can be stolen if not using HTTPS, and the server has to store the token

#session based auth > server stores the session data and sends a session ID to the client, which sends it with every request
#pros > secure, as the session data is stored on the server
#cons > server has to store the session data, which can be a performance issue for large applications

#JWT (JSON Web Token) > server generates a token that contains the user information and sends it to the client, which stores it and sends it with every request
# pros > Can carry user info,easy to scalble, stateless,rotate,blakclist tokens
# cons > large token size, can be stolen if not using HTTPS, server has to verify the token, loacl storage saves token, which can be a security risk if not using HTTPS

# OAUTH2.0 > third-party authentication service that allows users to log in using their existing accounts from other platforms (e.g., Google, Facebook)