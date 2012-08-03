import sys

from seaserv import get_org_id_by_repo_id
    
def access_org_repo(request, repo_id):
    """
    Check whether user can view org repo.
    """
    if not request.user.org:
        return False
    cur_org_id = request.user.org['org_id']
    org_id = get_org_id_by_repo_id(repo_id)
    return True if cur_org_id == org_id else False