<p align="center">
  <img src="bbncreative.svg" alt="bbncreative logotype" />
</p>

<br />

<p align="center">
    <a href="https://circleci.com/gh/aaroncawte/bbncreative-portfolio" target="blank" rel="noopener noreferrer">
        <img src="https://circleci.com/gh/aaroncawte/bbncreative-portfolio/tree/master.svg?style=svg&circle-token=dbf29770a59f46187030dc984ae4c03e1f988f42" alt="CircleCI" />
    </a>
</p>

# bbncreative-portfolio

A custom CMS and API for the bbncreative portfolio website, built with Django. The site runs at [bbncreative.co](https://bbncreative.co), and the API at `/api`.

This project, like the portfolio itself, is the work of Aaron Cawte. Contact Aaron via [email](mailto:aaron@bbncreative.co) or on [Twitter](https://twitter.com/aaroncawte).

## License

This software is made available for review. Accordingly, it is licensed under **Attribution-NonCommercial-NoDerivs 3.0 Unported (CC BY-NC-ND 3.0)**. View the license [here](/LICENSE.md), or view a summary on [creativecommons.org](https://creativecommons.org/licenses/by-nc-nd/3.0/).

## Stack

Primary tools and requirements used for this project.

| Function  | Tool       | Version | Updated    |
| :-------- | :--------- | :------ | :--------- |
| Language  | Python     | 3.8.2   | 09.05.2020 |
| Framework | Django     | 3.0.3   | 11.02.2020 |
| Database  | PostgreSQL | 10.5    | 23.08.2018 |

## Documentation

### Setup

The initial setup of this system has been documented for future reference, debugging and testing.

1. [Python virtual environment & Django installation](/docs/setup/virtualenv.md)
2. [Using PostgreSQL](/docs/setup/postgresql.md)
3. [Environment Variables](/docs/setup/envvars.md)
4. [Web Server Setup](/docs/setup/webserver.md)

### Reference

Relevant information to the system has also been documented as follows:

1. [Content Aspect Ratios](/docs/reference/aspect_ratios.md)

### API

Each API endpoint is documented with expected outputs following [this guidance](https://github.com/jamescooke/restapidocs).

* [Show Projects](/docs/api/projects.md) : `GET /api/projects/`
  * [Show Credits for Project](/docs/api/project/credits.md) : `GET /api/project/{project}/credits`
  * [Show Text Assets for Project](/docs/api/project/assets/text.md) : `GET /api/project/{project}/assets/text`
  * [Show Image Assets for Project](/docs/api/project/assets/image.md) : `GET /api/project/{project}/assets/image`
  * [Show Embedded Assets for Project](/docs/api/project/assets/embedded.md) : `GET /api/project/{project}/assets/embedded`
* [Show Feeds](/docs/api/feeds.md) : `GET /api/feeds/`
  * [Show Text Assets for Feed](/docs/api/feed/assets/text.md) : `GET /api/feed/{feed}/assets/text`
  * [Show Image Assets for Feed](/docs/api/feed/assets/image.md) : `GET /api/feed/{feed}/assets/image`
  * [Show Embedded Assets for Feed](/docs/api/feed/assets/embedded.md) : `GET /api/feed/{feed}/assets/embedded`
