add_executable(app main.cpp)

target_link_libraries(
  app PRIVATE spdlog::spdlog yaml-cpp::yaml-cpp argparse::argparse
              httplib::httplib nlohmann_json::nlohmann_json)
