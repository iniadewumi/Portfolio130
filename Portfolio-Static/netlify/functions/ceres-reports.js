// Ceres Reports serverless function
// In production, you could use a service like FaunaDB, Supabase, or a JSON file on S3
// For now, this returns the static JSON data and accepts new reports via POST

const fs = require('fs');
const path = require('path');

// In-memory store (resets on cold start - replace with a database for persistence)
let reports = [];

exports.handler = async (event) => {
  const headers = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
  };

  // Handle CORS preflight
  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 204, headers, body: '' };
  }

  // GET - Return all reports
  if (event.httpMethod === 'GET') {
    return {
      statusCode: 200,
      headers,
      body: JSON.stringify(reports),
    };
  }

  // POST - Create a new report
  if (event.httpMethod === 'POST') {
    try {
      const data = JSON.parse(event.body);
      const newReport = {
        id: Date.now(),
        text: data.text || '',
        created_at: data.date || new Date().toISOString(),
        modified_at: data.date || new Date().toISOString(),
      };
      reports.push(newReport);

      return {
        statusCode: 201,
        headers,
        body: JSON.stringify(newReport),
      };
    } catch (error) {
      return {
        statusCode: 400,
        headers,
        body: JSON.stringify({ error: 'Invalid request body' }),
      };
    }
  }

  return {
    statusCode: 405,
    headers,
    body: JSON.stringify({ error: 'Method not allowed' }),
  };
};
