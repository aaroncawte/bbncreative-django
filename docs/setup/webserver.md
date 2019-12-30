# 5. Web Server Setup

This complex process was based on [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04) from DigitalOcean.

Following from that, TLS was implemented using [this guide](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04).

Finally, HTTP2 was configured on nginx following [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-with-http-2-support-on-ubuntu-18-04#step-1-%E2%80%94-enabling-http2-support).

Along the way I:

- Added custom code to `/etc/nginx/sites-available/bbncreative` to get resources working on admin pages
- Customised that same file to get `www.` to redirect properly (Certbot handles the `http://` -> `https://` bit)
- Added server-side configuration to enable full CircleCI operability through SSH

## Changing Something?

- `/etc/nginx/sites-available/bbncreative` to configure nginx
- See the tutorial for anything else

## Changed Something?

- `sudo systemctl restart gunicorn` for changed Django config
- `sudo nginx -t` ensures nginx is configured correctly
- `sudo systemctl restart nginx` for changed nginx config

## Production Settings

There are some differences between the dev and production codebases, as follows:

- In `settings.py`:
  - `DEBUG = False`
  - `MEDIA_ROOT` = `/home/aaron/website/media/`
  - `MEDIA_URL` = `https://bbncreative.co/media/`
- Add `location /media/ { root /home/aaron/website/; }` to `etc/nginx/sites-available/bbncreative`
- `bbncreative/secrets.py` contains literal strings in production, where the development environment and CI use environment variables
- The Postgres password is different in production

## HTTP Headers

The HTTP headers for the server are declared in the nginx server file `/etc/nginx/sites-available/bbncreative`. They were on lines 31-37 and started with `add_header` when last modified.
When the headers are changed, the changes should be tested by first running:

```bash
sudo nginx -t
sudo systemctl nginx restart
```

Then, secondly, by viewing the console on the live website to ensure no CSP failures or other errors are reported.

**Note that references to the `sites-available/bbncreative` file should never be made to the `sites-enabled` symlink of the same file. Check [this StackOverflow answer](https://stackoverflow.com/questions/21812360/what-is-the-difference-between-sites-enabled-and-sites-available-directory) for more.**
