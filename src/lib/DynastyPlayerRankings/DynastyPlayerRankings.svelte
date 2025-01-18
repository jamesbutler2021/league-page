<!-- src/lib/DynastyRankings.svelte -->
<script>
  // You can import a store or any helpers here later when fetching the data.
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

  <!-- You can later add a table to display player data -->
  <table class="dynasty-table">
    <thead>
      <tr>
        <th>Player</th>
        <th>Position</th>
        <th>Value</th>
      </tr>
    </thead>
    <tbody>
      <!-- Player rows will be dynamically added here after data is fetched -->
    </tbody>
  </table>
</div>
