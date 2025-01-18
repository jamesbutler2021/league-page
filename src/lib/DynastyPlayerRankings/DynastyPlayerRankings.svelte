<!-- src/lib/DynastyRankings.svelte -->
<script>
  // Add logic for later (e.g., fetching data from the API)
</script>

<style>
  h1 {
    font-size: 2rem;
    margin-bottom: 20px;
  }

  .dynasty-table {
    width: 100%;
    border-collapse: collapse;
  }

  .dynasty-table th, .dynasty-table td {
    padding: 10px;
    border: 1px solid #ddd;
    text-align: left;
  }
</style>

<div>
  <h1>Dynasty Player Rankings</h1>
  <p>Data will be displayed here once fetched from the API.</p>

  <!-- Placeholder for displaying the rankings (you can update this later with dynamic data) -->
  <table class="dynasty-table">
    <thead>
      <tr>
        <th>Player</th>
        <th>Position</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      <!-- Player data will be inserted here dynamically -->
    </tbody>
  </table>
</div>
