<div class="chart-container">
                            <canvas id="salesChart"></canvas>
                        </div>
                    </div>

                    <!-- Recent activity -->
                    <div class="bg-white rounded-lg shadow p-6">
                        <h3 class="text-lg font-semibold mb-6">Recent Activity</h3>
                        <div class="space-y-4">
                            <div class="flex items-start">
                                <div class="p-2 bg-blue-100 text-blue-600 rounded-full mr-3">
                                    <i class="fas fa-file-invoice"></i>
                                </div>
                                <div>
                                    <p class="font-medium">New invoice received</p>
                                    <p class="text-sm text-gray-500">From Client A for $2,500</p>
                                    <p class="text-xs text-gray-400 mt-1">10 minutes ago</p>
                                </div>
                            </div>
                            <div class="flex items-start">
                                <div class="p-2 bg-green-100 text-green-600 rounded-full mr-3">
                                    <i class="fas fa-check-circle"></i>
                                </div>
                                <div>
                                    <p class="font-medium">Project completed</p>
                                    <p class="text-sm text-gray-500">Website redesign project</p>
                                    <p class="text-xs text-gray-400 mt-1">2 hours ago</p>
                                </div>
                            </div>
                            <div class="flex items-start">
                                <div class="p-2 bg-purple-100 text-purple-600 rounded-full mr-3">
                                    <i class="fas fa-user-plus"></i>
                                </div>
                                <div>
                                    <p class="font-medium">New team member</p>
                                    <p class="text-sm text-gray-500">John Smith joined the team</p>
                                    <p class="text-xs text-gray-400 mt-1">Yesterday</p>
                                </div>
                            </div>
                            <div class="flex items-start">
                                <div class="p-2 bg-yellow-100 text-yellow-600 rounded-full mr-3">
                                    <i class="fas fa-exclamation-triangle"></i>
                                </div>
                                <div>
                                    <p class="font-medium">Server issue</p>
                                    <p class="text-sm text-gray-500">Maintenance required</p>
                                    <p class="text-xs text-gray-400 mt-1">2 days ago</p>
                                </div>
                            </div>
                        </div>
                        <button class="w-full mt-4 py-2 text-blue-600 border border-blue-600 rounded-lg hover:bg-blue-50 transition">
                            View All Activity
                        </button>
                    </div>
                </div>

                <!-- Tasks and team members -->
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                    <!-- Tasks -->
                    <div class="bg-white rounded-lg shadow p-6">
                        <div class="flex items-center justify-between mb-6">
                            <h3 class="text-lg font-semibold">Tasks</h3>
                            <button class="text-blue-600 hover:text-blue-800">
                                <i class="fas fa-plus"></i> Add Task
                            </button>
                        </div>
                        <div class="space-y-4">
                            <div class="flex items-center">
                                <input type="checkbox" id="task1" class="task-checkbox hidden">
                                <label for="task1" class="task-label flex-1 flex items-center">
                                    <span class="w-4 h-4 border border-gray-300 rounded mr-3"></span>
                                    <span>Complete project proposal</span>
                                </label>
                                <span class="text-sm text-gray-500">Today</span>
                            </div>
                            <div class="flex items-center">
                                <input type="checkbox" id="task2" class="task-checkbox hidden" checked>
                                <label for="task2" class="task-label flex-1 flex items-center">
                                    <span class="w-4 h-4 border border-gray-300 rounded mr-3 bg-blue-500 border-blue-500 flex items-center justify-center text-white">
                                        <i class="fas fa-check text-xs"></i>
                                    </span>
                                    <span>Review client feedback</span>
                                </label>
                                <span class="text-sm text-gray-500">Yesterday</span>
                            </div>
                            <div class="flex items-center">
                                <input type="checkbox" id="task3" class="task-checkbox hidden">
                                <label for="task3" class="task-label flex-1 flex items-center">
                                    <span class="w-4 h-4 border border-gray-300 rounded mr-3"></span>
                                    <span>Update website content</span>
                                </label>
                                <span class="text-sm text-gray-500">Tomorrow</span>
                            </div>
                            <div class="flex items-center">
                                <input type="checkbox" id="task4" class="task-checkbox hidden">
                                <label for="task4" class="task-label flex-1 flex items-center">
                                    <span class="w-4 h-4 border border-gray-300 rounded mr-3"></span>
                                    <span>Prepare meeting agenda</span>
                                </label>
                                <span class="text-sm text-gray-500">Jun 15</span>
