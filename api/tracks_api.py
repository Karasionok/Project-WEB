from flask import Blueprint, jsonify

from data import db_session
from data.add import Track
from data.albums_py import Album
from data.singers_py import Singer
from data.track_user import TrackUser
from data.users_py import User

blueprint = Blueprint(
    'tracks_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/tracks/<int:user_id>')
def get_tracks(user_id):
    db_sess = db_session.create_session()
    track_list = []
    query = ((db_sess.query(Singer, Album, Track, User)
              .join(Album, Album.singer_id == Singer.id))
             .join(Track, Track.album_id == Album.id)
             .join(TrackUser, TrackUser.track_id == Track.id)
             .join(User, TrackUser.user_id == User.id)
             .filter(User.id == user_id))
    records = query.all()
    for singer, album, track, user in records:
        dict = {'id': track.id,
                'name': track.name,
                'singer': singer.name,
                'album': album.album_name,
                'duration': track.duration,
                'path': track.path}
        track_list.append(dict)
    return jsonify(track_list)

