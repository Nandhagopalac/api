const express = require('express');
const cors = require('cors');
const app = express();
const port = 3050;

app.use(cors());
app.use(express.json());

const db = require('./db');

// Get all users
app.get('/users', async (req, res) => {
  try {
    const users = await db.getUsers();
    res.json(users);
  } catch (err) {
    res.status(500).send(err.message);
  }
});

// Get a single user by ID
app.get('/users/:id', async (req, res) => {
  try {
    const user = await db.getUserById(parseInt(req.params.id));
    if (!user) return res.status(404).send('User not found.');
    res.json(user);
  } catch (err) {
    res.status(500).send(err.message);
  }
});

// Create a new user
app.post('/users', async (req, res) => {
  const { name, email } = req.body;
  if (!name || !email) {
    return res.status(400).send('Name and email are required.');
  }
  try {
    const newUser = await db.createUser(name, email);
    res.status(201).json(newUser);
  } catch (err) {
    res.status(500).send(err.message);
  }
});

// Update a user
app.put('/users/:id', async (req, res) => {
  const { name, email } = req.body;
  if (!name || !email) {
    return res.status(400).send('Name and email are required.');
  }
  try {
    const updatedUser = await db.updateUser(parseInt(req.params.id), name, email);
    if (!updatedUser) return res.status(404).send('User not found.');
    res.json(updatedUser);
  } catch (err) {
    res.status(500).send(err.message);
  }
});

// Delete a user
app.delete('/users/:id', async (req, res) => {
  try {
    await db.deleteUser(parseInt(req.params.id));
    res.status(204).send();
  } catch (err) {
    res.status(500).send(err.message);
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
