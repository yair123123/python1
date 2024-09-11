from operator import itemgetter

from toolz import pipe, compose
from toolz.curried import partial

from api.dbz_api import get_dbz
from repository.json_repository import read_json, convert_from_json_warrior, fight

if __name__ == '__main__':
    home_team = pipe(
        read_json("repository/home_team.json"),
        partial(map,lambda x: convert_from_json_warrior(x,type="home")),
        list
        )
    dbz_team = pipe(
        get_dbz("https://dragonball-api.com/api/characters/"),
        itemgetter("items"),
        partial(map,lambda x: convert_from_json_warrior(x,type="not_friend")),
        list
        )

    print(pipe(
        dbz_team,
        partial(map,lambda x: fight(x,home_team[x.uid])),
        partial(map,str),
        "\n".join
    ))
# first from home-team first from dbz-team
# check win according to ki

# first five against first five

# first ten against first ten (only uniq by affiliation )

# first against second only if they are not with the same affiliation

# write the description and the name upper case of the average warrior of each teams