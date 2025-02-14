from executables.acts.Base import BaseAct
from resources.Globals import yt_dlp, json, utils

class AExtractYoutubeStreams(BaseAct):
    name = 'AExtractYoutubeStreams'
    allow_type = 'all'
    type = 'string'

    def execute(self, args=None):
        url = args.get('input_entity', None)
        if url == None:
            raise ValueError("_error_no_url")

        dlp = yt_dlp.YoutubeDL({
            'listformats': True,
            'quiet': True
        })
        info = dlp.extract_info(url, download=False)
        json_data = dlp.sanitize_info(info)
        formatted_formats = []
        for format in json_data.get('formats'):
            formatted_formats.append({
                'format': format.get('format'),
                'format_id': format.get('format_id'),
                'format_note': format.get('format_note'),
                'fps': format.get('fps'),
                'quality': format.get('quality'),
                'vcodec': format.get('vcodec'),
                'acodec': format.get('acodec'),
                'resolution': format.get('resolution'),
                'abr': format.get('abr'),
                'vbr': format.get('vbr'),
                'video_ext': format.get('video_ext'),
                'audio_ext': format.get('audio_ext'),
            })

        return formatted_formats
