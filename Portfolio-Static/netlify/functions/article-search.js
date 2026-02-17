const https = require('https');

exports.handler = async (event) => {
  const keyword = event.queryStringParameters?.search_keyword;

  if (!keyword) {
    return {
      statusCode: 400,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ error: 'Missing search_keyword parameter' }),
    };
  }

  // API key is stored as a Netlify environment variable (set in Netlify dashboard)
  const apiKey = process.env.NEWS_API_KEY;

  if (!apiKey) {
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ error: 'API key not configured' }),
    };
  }

  const yesterday = new Date(Date.now() - 86400000).toISOString().split('T')[0];
  const url = `https://newsapi.org/v2/everything?q=${encodeURIComponent(keyword)}&apiKey=${apiKey}&from=${yesterday}&sortBy=relevancy&pageSize=20`;

  try {
    const data = await new Promise((resolve, reject) => {
      https.get(url, (res) => {
        let body = '';
        res.on('data', (chunk) => (body += chunk));
        res.on('end', () => resolve(JSON.parse(body)));
        res.on('error', reject);
      }).on('error', reject);
    });

    const articles = (data.articles || []).slice(0, 10).map((article) => ({
      source: article.source?.name || '',
      author: article.author || '',
      title: article.title || '',
      description: article.description || '',
      url: article.url || '',
      publishedAt: article.publishedAt || '',
      content: article.content
        ? article.content.split(' ').slice(0, 30).join(' ') + '...'
        : '',
    }));

    return {
      statusCode: 200,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
      },
      body: JSON.stringify({ articles }),
    };
  } catch (error) {
    return {
      statusCode: 500,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ error: 'Failed to fetch articles' }),
    };
  }
};
