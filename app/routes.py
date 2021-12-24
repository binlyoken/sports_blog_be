from app import api
from resource.user import MeResource, UserListResource, UserResource
from resource.signup import SignupResource
from resource.login import LoginResource
from resource.topic import TopicListResource, TopicResource

# Signup a acount
api.add_resource(SignupResource, "/v1/api/signup")
# Login to system
api.add_resource(LoginResource, "/v1/api/login")
# other api
api.add_resource(UserListResource, "/v1/api/account")
api.add_resource(UserResource, "/v1/api/account/<int:account_id>", "/v1/api/account")
api.add_resource(MeResource, "/v1/api/me")

# topic api
api.add_resource(TopicListResource, "/v1/api/topic")
api.add_resource(TopicResource, "/v1/api/topic/<int:topic_id>", "/v1/api/topic")
