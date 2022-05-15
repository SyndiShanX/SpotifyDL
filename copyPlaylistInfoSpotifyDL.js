// @ts-check
// NAME: copyPlaylistInfoSpotifyDL
// AUTHOR: SyndiShanX
// DESCRIPTION: Copy various information about the songs in your Playlist (Artist, Album Name, Date Added, Duration, Image URL, Song URL) ONLY USE with SpotifyDL.
/// <reference path="../globals.d.ts" />

(function copyPlaylistInfoMain() {
	
	function uriPlaylist(uris) {
		if (uris.length > 1) {
			return false;
		}
		const uri = uris[0];
		const uriObj = Spicetify.URI.fromString(uri);
		if (uriObj.type === Spicetify.URI.Type.PLAYLIST || uriObj.type === Spicetify.URI.Type.PLAYLIST_V2) 
			return true;
		return false;
    }
		
		function getArtists(songNum) {
			songArtists = tracks.items[songNum].artists[0].name.replaceAll('"', '').replaceAll("'", "\'").replaceAll('\\', '')
			for (x = 1; x < tracks.items[songNum].artists.length; x++) {
				songArtists = songArtists + ', ' + tracks.items[songNum].artists[x].name.replaceAll('"', '').replaceAll("'", "\'").replaceAll('\\', '')
			}
			songArtists = songArtists + '",\n'
			return songArtists
		}
	
	async function copyPlaylistInfo(uri) {
		playlist = await Spicetify.Platform.PlaylistAPI.getMetadata(uri)
		tracks = await Spicetify.Platform.PlaylistAPI.getContents(uri)
		synTracks = ''
		
		function millisToMinutesAndSeconds(millis) {
			var minutes = Math.floor(millis / 60000);
			var seconds = ((millis % 60000) / 1000).toFixed(0);
			return minutes + ":" + (seconds < 10 ? '0' : '') + seconds;
		}
		
		for (i = 0; i < tracks.items.length; i++) {
			synTracks = synTracks + '		{\n			"Song Name":  "' + tracks.items[i].name.replaceAll('"', '').replaceAll("'", "\'").replaceAll('\\', '') + '",\n' + '			"Artist":     "' + getArtists(i) + '			"Album Name": "' +tracks.items[i].album.name.replaceAll('"', '').replaceAll("'", "\'").replaceAll('\\', '') + '",\n' + '			"Date Added": "' + tracks.items[i].addedAt.toDateString().substring(4) + '",\n' + '			"Duration":   "' + millisToMinutesAndSeconds(tracks.items[i].duration.milliseconds) + '",\n' + '			"Image URL":  "https://i.scdn.co/image/' + tracks.items[i].album.images[0].url.split('image:')[1] + '",\n' + '			"Song URL":   "https://open.spotify.com/track/' + tracks.items[i].uri.split('track:')[1] + '"\n		},\n'
		}
		
		synPlaylist = '{\n	"Playlist": "' + playlist.name + '",\n  "Songs": [\n' + synTracks.slice(0, -2) + '\n  ]\n}'
		synPlaylist = synPlaylist.replaceAll('é', 'e').replaceAll('Ø', 'O').replaceAll('AC/DC', 'ACDC').replaceAll('Au/Ra', 'AuRa').replaceAll('Axwell / Ingrosso', 'Axwell  Ingrosso').replaceAll('Run–D.M.C.', 'Run D.M.C.').replaceAll('ö', 'o').replaceAll('ë', 'e').replaceAll('å', 'a').replaceAll('XXXTENTACION', 'XXXTentacion').replaceAll('SABAI', 'Sabai').replaceAll('Weird Al', "\'Weird Al\'").replaceAll("\'Weird Al\' Yankovic - Foil", "\'Weird Al\' Yankovic - Foil").replaceAll("Call of the Dead", "\'Call of the Dead\'").replaceAll("Ridin\'", "\'Ridin\'\'").replaceAll('Garrett Nash', 'gnash').replaceAll('Ü', 'U').replaceAll('á', 'a').replaceAll('?', '').replaceAll(' / ', '  ').replaceAll('Wreck-It Ralph/Soundtrack', "\'Wreck-It Ralph\'Soundtrack").replaceAll('’', "\'").replaceAll('TROLLS', '\'TROLLS\'').replaceAll('Friends', '\'Friends\'').replaceAll('8 Mile', '\'8 Mile\'').replaceAll('The Voice', '\'The Voice\'').replaceAll('.../...', '......').replaceAll('ñ', 'n').replaceAll('*', '').replaceAll('Man: Into', 'Man -  Into').replaceAll('Parody of Party In The USA', "Parody of \'Party In The U.S.A.\'").replaceAll('Armageddon', "\'Armageddon\'").replaceAll('Alice Through The Looking Glass', "\'Alice Through The Looking Glass\'")
		
		var synDiv = document.createElement('div');
		var synInput = document.createElement('textarea');
		
		synDiv.className = 'synDiv'
		synInput.className = 'synInput'
		
		synInput.value = synPlaylist
		
		synDiv.appendChild(synInput)
		document.getElementsByTagName('body')[0].appendChild(synDiv)
		
		var synCopy = document.getElementsByClassName('synInput')[0]
		synCopy.select();
		document.execCommand('copy');
		
		synDiv.remove()
	}
	
	new Spicetify.ContextMenu.Item("Copy Playlist Info", copyPlaylistInfo, uriPlaylist, `<svg role="img" height="16" width="16" viewBox="0 0 16 16" fill="currentColor"><path d="M8.492 6.619a.522.522 0 00.058.737c.45.385.723.921.77 1.511.046.59-.14 1.163-.524 1.613l-2.372 2.777c-.385.45-.921.724-1.512.77a2.21 2.21 0 01-1.613-.524 2.22 2.22 0 01-.246-3.125l1.482-1.735a.522.522 0 10-.795-.679L2.259 9.7a3.266 3.266 0 00.362 4.599 3.237 3.237 0 002.374.771 3.234 3.234 0 002.224-1.134l2.372-2.777c.566-.663.84-1.505.771-2.375A3.238 3.238 0 009.228 6.56a.523.523 0 00-.736.059zm4.887-4.918A3.233 3.233 0 0011.004.93 3.234 3.234 0 008.78 2.064L6.409 4.84a3.241 3.241 0 00-.772 2.374 3.238 3.238 0 001.134 2.224.519.519 0 00.738-.058.522.522 0 00-.058-.737 2.198 2.198 0 01-.771-1.511 2.208 2.208 0 01.524-1.613l2.372-2.777c.385-.45.921-.724 1.512-.77a2.206 2.206 0 011.613.524 2.22 2.22 0 01.246 3.125l-1.482 1.735a.522.522 0 10.795.679L13.741 6.3a3.266 3.266 0 00-.362-4.599z"></path></svg>`).register();
	
})();