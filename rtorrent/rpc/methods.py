# Copyright (c) 2011 Chris Lucas, <cjlucas07@gmail.com>
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
""" Collection of categorized XMLRPC functions """

retrievers = {
 'file': {
          'get_completed_chunks': ('f.get_completed_chunks', None),
          'get_frozen_path': ('f.get_frozen_path', None),
          'get_last_touched': ('f.get_last_touched', None),
          'get_match_depth_next': ('f.get_match_depth_next', None),
          'get_match_depth_prev': ('f.get_match_depth_prev', None),
          'get_offset': ('f.get_offset', None),
          'get_path': ('f.get_path', None),
          'get_path_components': ('f.get_path_components', None),
          'get_path_depth': ('f.get_path_depth', None),
          'get_priority': ('f.get_priority', None),
          'get_range_first': ('f.get_range_first', None),
          'get_range_second': ('f.get_range_second', None),
          'get_size_bytes': ('f.get_size_bytes', None),
          'get_size_chunks': ('f.get_size_chunks', None),
          'is_create_queued': ('f.is_create_queued', None, True),
          'is_created': ('f.is_created', None, True),
          'is_open': ('f.is_open', None, True),
          'is_resize_queued': ('f.is_resize_queued', None, True)
          },
 'general': {
             'get_bind': ('get_bind', None),
             'get_check_hash': ('get_check_hash', None),
             'get_connection_leech': ('get_connection_leech', None),
             'get_connection_seed': ('get_connection_seed', None),
             'get_dht_port': ('get_dht_port', None),
             'get_dht_throttle': ('get_dht_throttle', None),
             'get_directory': ('get_directory', None),
             'get_down_rate': ('get_down_rate', None),
             'get_down_total': ('get_down_total', None),
             'get_download_rate': ('get_download_rate', None),
             'get_handshake_log': ('get_handshake_log', None),
             'get_hash_interval': ('get_hash_interval', None),
             'get_hash_max_tries': ('get_hash_max_tries', None),
             'get_hash_read_ahead': ('get_hash_read_ahead', None),
             'get_http_cacert': ('get_http_cacert', None),
             'get_http_capath': ('get_http_capath', None),
             'get_http_proxy': ('get_http_proxy', None),
             'get_ip': ('get_ip', None),
             'get_log.tracker': ('get_log.tracker', None),
             'get_max_downloads_div': ('get_max_downloads_div', None),
             'get_max_downloads_global': ('get_max_downloads_global', None),
             'get_max_file_size': ('get_max_file_size', None),
             'get_max_memory_usage': ('get_max_memory_usage', None),
             'get_max_open_files': ('get_max_open_files', None),
             'get_max_open_http': ('get_max_open_http', None),
             'get_max_open_sockets': ('get_max_open_sockets', None),
             'get_max_peers': ('get_max_peers', None),
             'get_max_peers_seed': ('get_max_peers_seed', None),
             'get_max_uploads': ('get_max_uploads', None),
             'get_max_uploads_div': ('get_max_uploads_div', None),
             'get_max_uploads_global': ('get_max_uploads_global', None),
             'get_memory_usage': ('get_memory_usage', None),
             'get_min_peers': ('get_min_peers', None),
             'get_min_peers_seed': ('get_min_peers_seed', None),
             'get_name': ('get_name', None),
             'get_peer_exchange': ('get_peer_exchange', None),
             'get_port_open': ('get_port_open', None),
             'get_port_random': ('get_port_random', None),
             'get_port_range': ('get_port_range', None),
             'get_preload_min_size': ('get_preload_min_size', None),
             'get_preload_required_rate': ('get_preload_required_rate', None),
             'get_preload_type': ('get_preload_type', None),
             'get_proxy_address': ('get_proxy_address', None),
             'get_receive_buffer_size': ('get_receive_buffer_size', None),
             'get_safe_sync': ('get_safe_sync', None),
             'get_scgi_dont_route': ('get_scgi_dont_route', None),
             'get_send_buffer_size': ('get_send_buffer_size', None),
             'get_session': ('get_session', None),
             'get_session_lock': ('get_session_lock', None),
             'get_session_on_completion': ('get_session_on_completion', None),
             'get_split_file_size': ('get_split_file_size', None),
             'get_split_suffix': ('get_split_suffix', None),
             'get_stats_not_preloaded': ('get_stats_not_preloaded', None),
             'get_stats_preloaded': ('get_stats_preloaded', None),
             ## get_throttle_* functions cause xmlrpc to throw Fault
             #'get_throttle_down_max': ('get_throttle_down_max', None),
             #'get_throttle_down_rate': ('get_throttle_down_rate', None),
             #'get_throttle_up_max': ('get_throttle_up_max', None),
             #'get_throttle_up_rate': ('get_throttle_up_rate', None),
             'get_timeout_safe_sync': ('get_timeout_safe_sync', None),
             'get_timeout_sync': ('get_timeout_sync', None),
             'get_tracker_numwant': ('get_tracker_numwant', None),
             'get_up_rate': ('get_up_rate', None),
             'get_up_total': ('get_up_total', None),
             'get_upload_rate': ('get_upload_rate', None),
             'get_use_udp_trackers': ('get_use_udp_trackers', None),
             'get_xmlrpc_size_limit': ('get_xmlrpc_size_limit', None)
             },
 'peer': {
          'banned': ('p.banned', None),
          'client_version': ('p.client_version', None),
          'completed_percent': ('p.completed_percent', None),
          'get_address': ('p.get_address', None),
          'get_client_version': ('p.get_client_version', None),
          'get_completed_percent': ('p.get_completed_percent', None),
          'get_down_rate': ('p.get_down_rate', None),
          'get_down_total': ('p.get_down_total', None),
          'get_id': ('p.get_id', None),
          'get_id_html': ('p.get_id_html', None),
          'get_options_str': ('p.get_options_str', None),
          'get_peer_rate': ('p.get_peer_rate', None),
          'get_peer_total': ('p.get_peer_total', None),
          'get_port': ('p.get_port', None),
          'get_up_rate': ('p.get_up_rate', None),
          'get_up_total': ('p.get_up_total', None),
          'is_encrypted': ('p.is_encrypted', None, True),
          'is_incoming': ('p.is_incoming', None, True),
          'is_obfuscated': ('p.is_obfuscated', None, True),
          'is_preferred': ('p.is_preferred', None, True),
          'is_snubbed': ('p.is_snubbed', None, True),
          'is_unwanted': ('p.is_unwanted', None, True)
          },
 'torrent': {
             'get_base_filename': ('d.get_base_filename', None),
             'get_base_path': ('d.get_base_path', None),
             'get_bitfield': ('d.get_bitfield', None),
             'get_bytes_done': ('d.get_bytes_done', None),
             'get_chunk_size': ('d.get_chunk_size', None),
             'get_chunks_hashed': ('d.get_chunks_hashed', None),
             'get_complete': ('d.get_complete', None),
             'get_completed_bytes': ('d.get_completed_bytes', None),
             'get_completed_chunks': ('d.get_completed_chunks', None),
             'get_connection_current': ('d.get_connection_current', None),
             'get_connection_leech': ('d.get_connection_leech', None),
             'get_connection_seed': ('d.get_connection_seed', None),
             'get_creation_date': ('d.get_creation_date', None),
             'get_directory': ('d.get_directory', None),
             'get_directory_base': ('d.get_directory_base', None),
             'get_down_rate': ('d.get_down_rate', None),
             'get_down_total': ('d.get_down_total', None),
             'get_free_diskspace': ('d.get_free_diskspace', None),
             'get_hashing': ('d.get_hashing', None),
             'get_hashing_failed': ('d.get_hashing_failed', None),
             'get_ignore_commands': ('d.get_ignore_commands', None),
             'get_left_bytes': ('d.get_left_bytes', None),
             'get_loaded_file': ('d.get_loaded_file', None),
             'get_local_id': ('d.get_local_id', None),
             'get_local_id_html': ('d.get_local_id_html', None),
             'get_max_file_size': ('d.get_max_file_size', None),
             'get_max_size_pex': ('d.get_max_size_pex', None),
             'get_message': ('d.get_message', None),
             'get_name': ('d.get_name', None),
             'get_peer_exchange': ('d.get_peer_exchange', None),
             'get_peers_accounted': ('d.get_peers_accounted', None),
             'get_peers_complete': ('d.get_peers_complete', None),
             'get_peers_connected': ('d.get_peers_connected', None),
             'get_peers_max': ('d.get_peers_max', None),
             'get_peers_min': ('d.get_peers_min', None),
             'get_peers_not_connected': ('d.get_peers_not_connected', None),
             'get_priority': ('d.get_priority', None),
             'get_priority_str': ('d.get_priority_str', None),
             'get_ratio': ('d.get_ratio', None),
             'get_size_bytes': ('d.get_size_bytes', None),
             'get_size_chunks': ('d.get_size_chunks', None),
             'get_size_files': ('d.get_size_files', None),
             'get_size_pex': ('d.get_size_pex', None),
             'get_skip_rate': ('d.get_skip_rate', None),
             'get_skip_total': ('d.get_skip_total', None),
             'get_state': ('d.get_state', None),
             'get_state_changed': ('d.get_state_changed', None),
             'get_state_counter': ('d.get_state_counter', None),
             'get_throttle_name': ('d.get_throttle_name', None),
             'get_tied_to_file': ('d.get_tied_to_file', None),
             'get_tracker_focus': ('d.get_tracker_focus', None),
             'get_tracker_numwant': ('d.get_tracker_numwant', None),
             'get_tracker_size': ('d.get_tracker_size', None),
             'get_up_rate': ('d.get_up_rate', None),
             'get_up_total': ('d.get_up_total', None),
             'get_uploads_max': ('d.get_uploads_max', None),
             'incomplete': ('d.incomplete', None),
             'is_active': ('d.is_active', None, True),
             'is_hash_checked': ('d.is_hash_checked', None, True),
             'is_hash_checking': ('d.is_hash_checking', None, True),
             'is_multi_file': ('d.is_multi_file', None, True),
             'is_open': ('d.is_open', None, True),
             'is_pex_active': ('d.is_pex_active', None, True),
             'is_private': ('d.is_private', None, True)
             },
 'tracker': {
             'get_group': ('t.get_group', None),
             'get_id': ('t.get_id', None),
             'get_min_interval': ('t.get_min_interval', None),
             'get_normal_interval': ('t.get_normal_interval', None),
             'get_scrape_complete': ('t.get_scrape_complete', None),
             'get_scrape_downloaded': ('t.get_scrape_downloaded', None),
             'get_scrape_incomplete': ('t.get_scrape_incomplete', None),
             'get_scrape_time_last': ('t.get_scrape_time_last', None),
             'get_type': ('t.get_type', None),
             'get_url': ('t.get_url', None),
             'is_enabled': ('t.is_enabled', None, True),
             'is_open': ('t.is_open', None, True)
             }
}

modifiers = {
		# syntax: name_of_local_function : (name_of_rpc_function, docstring)
		"general" : {
					"set_bind" : (
								"set_bind",
								"""Set address bind
								
								@param arg: ip address
								@type arg: str"""
								),
					"set_ip" : (
								"set_ip",
								"""Set IP
								
								@param arg: ip address
								@type arg: str"""
								),
					"set_download_limit" : (
								"set_download_rate",
								"""Set global download limit (in bytes)
								
								@param arg: speed limit
								@type arg: int
								"""
								),
					"set_upload_limit" : (
								"set_upload_rate",
								"""Set global upload limit (in bytes)
								
								@param arg: speed limit
								@type arg: int
								"""
								),
					#"set_bind" : ("set_bind", None),
					#"set_check_hash" : ("set_check_hash", None),
					"set_connection_leech" : ("set_connection_leech", None),
					"set_connection_seed" : ("set_connection_seed", None),
					#"set_dht_port" : ("set_dht_port", None),
					"set_dht_throttle" : ("set_dht_throttle", None),
					"set_directory" : ("set_directory", None),
					#"set_download_rate" : ("set_download_rate", None),
					"set_handshake_log" : ("set_handshake_log", None),
					"set_hash_interval" : ("set_hash_interval", None),
					"set_hash_max_tries" : ("set_hash_max_tries", None),
					"set_hash_read_ahead" : ("set_hash_read_ahead", None),
					"set_http_cacert" : ("set_http_cacert", None),
					"set_http_capath" : ("set_http_capath", None),
					"set_http_proxy" : ("set_http_proxy", None),
					#"set_ip" : ("set_ip", None),
					"set_log.tracker" : ("set_log.tracker", None),
					"set_max_downloads_div" : ("set_max_downloads_div", None),
					"set_max_downloads_global" : ("set_max_downloads_global", None),
					"set_max_file_size" : ("set_max_file_size", None),
					"set_max_memory_usage" : ("set_max_memory_usage", None),
					"set_max_open_files" : ("set_max_open_files", None),
					"set_max_open_http" : ("set_max_open_http", None),
					"set_max_peers" : ("set_max_peers", None),
					"set_max_peers_seed" : ("set_max_peers_seed", None),
					"set_max_uploads" : ("set_max_uploads", None),
					"set_max_uploads_div" : ("set_max_uploads_div", None),
					"set_max_uploads_global" : ("set_max_uploads_global", None),
					"set_min_peers" : ("set_min_peers", None),
					"set_min_peers_seed" : ("set_min_peers_seed", None),
					"set_name" : ("set_name", None),
					"set_peer_exchange" : ("set_peer_exchange", None),
					"set_port_open" : ("set_port_open", None),
					"set_port_random" : ("set_port_random", None),
					"set_port_range" : ("set_port_range", None),
					"set_preload_min_size" : ("set_preload_min_size", None),
					"set_preload_required_rate" : ("set_preload_required_rate", None),
					"set_preload_type" : ("set_preload_type", None),
					"set_proxy_address" : ("set_proxy_address", None),
					"set_receive_buffer_size" : ("set_receive_buffer_size", None),
					"set_safe_sync" : ("set_safe_sync", None),
					"set_scgi_dont_route" : ("set_scgi_dont_route", None),
					"set_send_buffer_size" : ("set_send_buffer_size", None),
					"set_session" : ("set_session", None),
					"set_session_lock" : ("set_session_lock", None),
					"set_session_on_completion" : ("set_session_on_completion", None),
					"set_split_file_size" : ("set_split_file_size", None),
					"set_split_suffix" : ("set_split_suffix", None),
					"set_timeout_safe_sync" : ("set_timeout_safe_sync", None),
					"set_timeout_sync" : ("set_timeout_sync", None),
					"set_tracker_numwant" : ("set_tracker_numwant", None),
					#"set_upload_rate" : ("set_upload_rate", None),
					"set_use_udp_trackers" : ("set_use_udp_trackers", None),
					"set_xmlrpc_dialect" : ("set_xmlrpc_dialect", None),
					"set_xmlrpc_size_limit" : ("set_xmlrpc_size_limit", None),
		},
        "torrent" : {
                    "set_connection_current" : ("d.set_connection_current", None),
                    "set_custom" : ("d.set_custom", None),
                    "set_custom1" : ("d.set_custom1", None),
                    "set_custom2" : ("d.set_custom2", None),
                    "set_custom3" : ("d.set_custom3", None),
                    "set_custom4" : ("d.set_custom4", None),
                    "set_custom5" : ("d.set_custom5", None),
                    #"set_directory" : ("d.set_directory", None),
                    #"set_directory_base" : ("d.set_directory_base", None),
                    "set_hashing_failed" : ("d.set_hashing_failed", None),
                    "set_ignore_commands" : ("d.set_ignore_commands", None),
                    "set_max_file_size" : ("d.set_max_file_size", None),
                    "set_message" : ("d.set_message", None),
                    "set_peers_max" : ("d.set_peers_max", None),
                    "set_peers_min" : ("d.set_peers_min", None),
                    "set_priority" : ("d.set_priority", None),
                    "set_throttle_name" : ("d.set_throttle_name", None),
                    "set_tied_to_file" : ("d.set_tied_to_file", None),
                    "set_tracker_numwant" : ("d.set_tracker_numwant", None),
                    "set_uploads_max" : ("d.set_uploads_max", None),
        },
        "tracker" : {
                     #"disable" : ("t.disable", None),
                     #"enable" : ("t.enable", None),
                     "set_enabled" : ("t.set_enabled", None),

        },
        "peer" : {
        },
		"file" : {
		}
}